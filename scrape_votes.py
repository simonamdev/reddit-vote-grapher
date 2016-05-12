#!/usr/bin/python3

import time
import os
import csv
import praw
import OAuth2Util
from pprint import pprint


class SubmissionCSV:
    def __init__(self, file_name='', csv_directory='data'):
        self.file_name = file_name + '.csv'
        self.file_path = os.path.join(os.getcwd(), csv_directory, self.file_name)

    def run(self, data_row=None):
        self.create_csv()
        if data_row is not None:
            self.write_row(row=data_row)

    def create_csv(self):
        # create the CSV if it does not exist
        if not os.path.isfile(self.file_path):
            with open(self.file_path, mode='w', newline='') as csvfile:
                csvfile.flush()
            time.sleep(1)

    def write_row(self, row=None):
        if row is not None:
            with open(self.file_path, mode='a', newline='') as csvfile:
                writer = csv.writer(csvfile, quotechar='"')
                writer.writerow(row)
                csvfile.flush()


class VoteScraper:
    def __init__(self, user_agent='vote-grapher-v1-by-Always_SFW', subreddit='EliteDangerous', verbose=True):
        self.user_agent = user_agent
        self.subreddit_name = subreddit
        self.verbose = verbose
        self.r = None
        self.o = None
        self.subreddit = None
        self.submission_limit = 15
        # holds the objects for cached submissions. This is rebuilt every time the script starts from
        # the names of the CSV files
        self.cached_submissions = []

    def run(self):
        self.connect()
        while True:
            self.cache_new_submissions()
            self.remove_old_submissions()
            self.store_submissions_data()
            self.print('Pausing for 120 seconds')
            time.sleep(120)

    def print(self, string=''):
        if self.verbose:
            print(string)

    def connect(self):
        # initialise a connection to reddit
        self.print('Initialising connection to Reddit')
        self.r = praw.Reddit(self.user_agent)
        self.o = OAuth2Util.OAuth2Util(self.r)
        self.print('Successfully connected to Reddit.')
        self.subreddit = self.r.get_subreddit(subreddit_name=self.subreddit_name)

    def get_latest_submissions(self):
        self.print('Getting latest submissions')
        new_submissions = self.subreddit.get_new(limit=self.submission_limit)
        return new_submissions

    def cache_new_submissions(self):
        new_submissions = self.get_latest_submissions()
        self.print('Caching new submissions')
        previous_count = len(self.cached_submissions)
        for submission in new_submissions:
            if submission not in self.cached_submissions:
                self.cached_submissions.append(submission)
        self.print('{} new submissions recorded'.format(len(self.cached_submissions) - previous_count))

    def remove_old_submissions(self):
        self.print('Removing old submissions')
        current_time = time.mktime(time.gmtime())
        to_remove = []
        previous_count = len(self.cached_submissions)
        for submission in self.cached_submissions:
            if (current_time - submission.created_utc) > (12 * 60 * 60):
                self.print('Removing Submission with ID: {} as it is older than 12 hours'.format(submission.id))
                to_remove.append(submission)
        self.cached_submissions = [sub for sub in self.cached_submissions if sub not in to_remove]
        self.print('{} old submissions removed'.format(len(self.cached_submissions) - previous_count))

    def store_submissions_data(self):
        for i, sub in enumerate(self.cached_submissions):
            sub.refresh()
            ratio = self.r.get_submission(sub.permalink).upvote_ratio
            ups = int(round((ratio*sub.score)/(2*ratio - 1)) if ratio != 0.5 else round(sub.score/2))
            downs = ups - sub.score
            self.print('[{}] ID: {} Score: {} Up: {} Down: {} Ratio: {} Link: {} Age: {} hours'.format(
                    i,
                    sub.id,
                    sub.score,
                    ups,
                    downs,
                    ratio,
                    sub.short_link,
                    abs(round((time.mktime(time.gmtime()) - sub.created_utc) / (60 * 60), 2))))
            subcsv = SubmissionCSV(file_name=sub.id)
            subcsv.run(data_row=[time.mktime(time.gmtime()), sub.score, ups, downs, ratio])
            time.sleep(2)


def main():
    v = VoteScraper()
    v.run()

if __name__ == '__main__':
    main()

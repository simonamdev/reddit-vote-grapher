#!/usr/bin/python3

import os
import csv
import praw
import OAuth2Util
from pprint import pprint
from time import sleep


class SubmissionCSV:
    def __init__(self, file_name='', csv_directory='data'):
        self.file_name = file_name + '.csv'
        self.file_path = os.path.join(os.getcwd(), csv_directory, self.file_name)

    def run(self):
        self.create_csv()

    def create_csv(self):
        # create the CSV if it does not exist
        if not os.path.isfile(self.file_path):
            with open(self.file_path, mode='w', newline='') as csvfile:
                csvfile.flush()

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
        # holds the objects for cached submissions. This is rebuilt every time the script starts from
        # the names of the CSV files
        self.cached_submissions = []

    def run(self):
        self.connect()
        self.get_latest_submissions()

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
        new_submissions = self.subreddit.get_new(limit=150)
        for i, sub in enumerate(new_submissions):
            ratio = self.r.get_submission(sub.permalink).upvote_ratio
            ups = int(round((ratio*sub.score)/(2*ratio - 1)) if ratio != 0.5 else round(sub.score/2))
            downs = ups - sub.score
            self.print('[{}] ID: {} Score: {} Up: {} Down: {} Ratio: {} Link: {}'.format(
                    i,
                    sub.id,
                    sub.score,
                    ups,
                    downs,
                    ratio,
                    sub.short_link))
            sleep(1)


def main():
    v = VoteScraper()
    v.run()

if __name__ == '__main__':
    main()

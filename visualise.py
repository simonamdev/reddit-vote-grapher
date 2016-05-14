import os
import csv
from flask import Flask, render_template
app = Flask(__name__)


def return_file_list():
    files_dir = os.path.join(os.getcwd(), 'data')
    csv_files = os.listdir(files_dir)
    print('Found {} CSV files'.format(len(csv_files)))
    return csv_files


"""
file_data = dict()
csv_path = os.path.join(os.getcwd(), 'data', file)
file_data['name'] = file
file_data['path'] = csv_path
file_data['rows'] = []
with open(csv_path, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
        file_data['rows'].append(row)
print(file_data)
file_data_list.append(file_data)
"""


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/refresh')
def refresh():
    return 'refreshed'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=5000, debug=False)

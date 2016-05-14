import os
import csv
from flask import Flask, render_template
app = Flask(__name__)


def return_file_data():
    files_dir = os.path.join(os.getcwd(), 'data')
    csv_files = os.listdir(files_dir)
    file_data_list = []
    for file in csv_files:
        file_data = dict()
        file_data['name'] = file.replace('.csv', '').replace('_complete', '')
        file_data['path'] = os.path.join(files_dir, file)
        file_data['complete'] = True if 'complete' in file else False
        file_data_list.append(file_data)
    return file_data_list


"""
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
    return render_template('index.html', file_data=return_file_data())


@app.route('/refresh')
def refresh():
    return 'refreshed'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=5000, debug=False)

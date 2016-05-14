import os
import csv
import datetime
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

file_data_list = []


def cache_file_data():
    global file_data_list
    files_dir = os.path.join(os.getcwd(), 'data')
    csv_files = os.listdir(files_dir)
    for file in csv_files:
        file_data = dict()
        file_data['name'] = file.replace('.csv', '').replace('_complete', '')
        file_data['path'] = os.path.join(files_dir, file)
        file_data['complete'] = True if 'complete' in file else False
        with open(file_data['path'], mode='r') as csvfile:
            csvreader = csv.reader(csvfile)
            data_list = list(csvreader)
            file_data['age'] = round((float(data_list[-1][0]) - float(data_list[0][0])) / (60 * 60), 2)
            file_data['last_read'] = datetime.datetime.fromtimestamp(int(float(data_list[-1][0]))).strftime('%d/%m/%Y @ %H:%M:%S')
        file_data_list.append(file_data)


@app.route('/')
def index():
    global file_data_list
    return render_template('index.html', file_data=file_data_list)


@app.route('/refresh')
def refresh_data():
    cache_file_data()
    return redirect(url_for('index'))


@app.route('/graph/<name>')
def graph(name):
    return name


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=5000, debug=False)

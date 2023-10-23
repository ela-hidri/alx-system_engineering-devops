#!/usr/bin/python3
""" export data in the CSV format. """
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    with open('{}.csv'.format(argv[1]), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([task.get('userId'),
                             user.get('name'),
                             task.get('completed'),
                             task.get('title')])
        file.close()

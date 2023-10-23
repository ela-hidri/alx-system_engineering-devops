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
    with open('{}.json'.format(argv[1]), "w") as outfile:
        json.dump({user.get('id'): [{
                  "task": t.get('title'),
                  "completed": t.get('completed'),
                  "username": user.get('username')
                  }for t in todos]},
                  outfile)
        outfile.close()

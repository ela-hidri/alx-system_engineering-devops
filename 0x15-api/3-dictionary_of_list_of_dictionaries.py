#!/usr/bin/python3
""" export data in the CSV format. """
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + "users").json()
    with open('todo_all_employees.json', "w") as outfile:
        for u in users:
            id = u.get('id')
            todos = requests.get(url + "todos", params={"userId": id}).json()
            json.dump({id: [{
                      "username": u.get('username'),
                      "task": t.get('title'),
                      "completed": t.get('completed')
                      }for t in todos]},
                      outfile)
    outfile.close()

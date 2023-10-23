#!/usr/bin/python3
""" export data in the CSV format. """
import csv
import json
import requests
from sys import argv


def todos(id):
    """ get todos """
    url = 'https://jsonplaceholder.typicode.com/'
    return requests.get(url + "todos", params={"userId": id}).json()


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + "users").json()
    with open('todo_all_employees.json', "w") as outfile:
        json.dump({u.get("id"): [{
                  "username": u.get("username"),
                  "task": t.get("title"),
                  "completed": t.get("completed")
                  } for t in todos(u.get("id"))]
                  for u in users}, outfile)
    oufile.close()

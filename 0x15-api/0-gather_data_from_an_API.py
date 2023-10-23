#!/usr/bin/python3
"""  returns information about his/her TODO list progress. """
import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        url = 'https://jsonplaceholder.typicode.com/'
        user = requests.get(url + "users/{}".format(argv[1])).json()
        todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
        cmpl = [t.get('title') for t in todos if t.get('completed') is True]
        print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
                                                              len(cmpl),
                                                              len(todos)))
        [print("\t {}".format(task)) for task in cmpl]

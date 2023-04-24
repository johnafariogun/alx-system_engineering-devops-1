#!/usr/bin/python3
"""
Python script that interacts with a REST api and returns information"""

from sys import argv
import json
import requests


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    users = requests.get('{}/users'.format(API)).json()
    task = requests.get('{}/todos'.format(API)).json()
    data = {}
    for user in users:
        id = user.get('id')
        username = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, task))
        user_data = list(map(lambda user: {"username": username,
                         "task": user.get("title"),
                         "completed": user.get("completed")}, todos))
        data["{}".format(id)] = user_data
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)

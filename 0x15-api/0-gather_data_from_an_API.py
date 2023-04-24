#!/usr/bin/python3
"""
Python script that interacts with a REST api and returns information"""

import requests
from sys import argv


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(argv) > 1:
        id = int(argv[1])
        user_res = requests.get('{}/users/{}'.format(API, id)).json()
        task = requests.get('{}/todos'.format(API)).json()
        username = user_res.get('name')
        todos = list(filter(lambda x: x.get('userId') == id, task))
        task_done = list(filter(lambda x: x.get('completed'), todos))
        print(
            'Employee {} is done with tasks({}/{}):'.format(
                username,
                len(task_done),
                len(todos)
            )
        )
        for todo_done in task_done:
            print('\t {}'.format(todo_done.get('title')))

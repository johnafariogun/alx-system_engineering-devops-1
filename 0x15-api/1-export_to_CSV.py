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
        username = user_res.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, task))
        with open('{}.csv'.format(id), 'w') as f:
            for todo in todos:
                f.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            username,
                            todo.get('completed'),
                            todo.get('title')
                            ))

#!/usr/bin/python3
"""
Python script that interacts with a REST api and returns information"""

from sys import argv
import json
import requests


API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(argv) > 1:
        id = int(argv[1])
        user = requests.get('{}/users/{}'.format(API, id)).json()
        task = requests.get('{}/todos'.format(API)).json()
        username = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, task))
        with open('{}.json'.format(id), 'w') as f:
            data = list(map(lambda user:
                        {"task": user.get("title"),
                            "completed": user.get("completed"),
                            "username": username},
                todos))
            data = {
                    "{}".format(id): data
                    }
            json.dump(data, f)

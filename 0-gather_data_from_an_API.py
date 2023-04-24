#!/usr/bin/python3
"""
Python script that interacts with a REST api and returns information"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        user = argv[1]
        request = requests.
        get("https://jsonplaceholder.typicode.com/users/{}"
            .format(user))
        name = request.json().get("name")
        if name is not None:
            todos = requests.get("https://jsonplaceholder.typicode.com/\
                    todos?userId={}".format(user)).json()
            allTasks = len(todos)
            completed = []
            for task in todos:
                if task.get("completed"):
                    completed.append(task)
            num = len(completed)
            print("Employee {} is done with task({}/{}):"
                  .format(name, num, allTasks))
            for title in completed:
                print("\t {}".format(title.get("title")))

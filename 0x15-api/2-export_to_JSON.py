#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
from sys import argv


def to_json():
    """return API data"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            USERNAME = (user.get('username'))
            break
    TASK_STATUS_TITLE = []

    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for task in todos.json():
        if task.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((task.get('completed'),
                                      task.get('title')))

    """export to json"""
    info = []
    for task in TASK_STATUS_TITLE:
        info.append({"task": task[1], "completed": task[0],
                     "username": USERNAME})
    data = {str(argv[1]): info}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    to_json()

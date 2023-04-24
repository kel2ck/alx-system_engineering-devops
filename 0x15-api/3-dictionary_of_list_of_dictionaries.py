#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


def all_to_json():
    """return API data"""
    USERS = []
    userss = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in userss.json():
        USERS.append((user.get('id'), user.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for task in todos.json():
        TASK_STATUS_TITLE.append((task.get('userId'),
                                  task.get('completed'),
                                  task.get('title')))

    """export to json"""
    data = dict()
    for user in USERS:
        t = []
        for task in TASK_STATUS_TITLE:
            if task[0] == user[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": user[1]})
        data[str(user[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)


if __name__ == "__main__":
    all_to_json()

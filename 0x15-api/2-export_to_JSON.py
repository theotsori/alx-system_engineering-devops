#!/usr/bin/python3
"""
Export data in the JSON format.

Records all tasks that are owned by this employee.
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
                  "completed": TASK_COMPLETED_STATUS,
                  "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user_response = requests.get(user_url)
    tasks_response = requests.get(tasks_url)

    user_data = user_response.json()
    tasks_data = tasks_response.json()

    username = user_data.get("username")
    tasks = []

    for task in tasks_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks.append(task_dict)

    data = {user_id: tasks}
    filename = "{}.json".format(user_id)

    with open(filename, mode="w") as f:
        json.dump(data, f)

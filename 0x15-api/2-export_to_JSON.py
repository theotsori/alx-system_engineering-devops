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
import sys


if __name__ == "__main__":
    # Get user id from command line argument
    user_id = sys.argv[1]

    # Build URLs for user and tasks
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    # Send requests and get responses
    user_response = requests.get(user_url)
    tasks_response = requests.get(tasks_url)

    # Get JSON data from responses
    user_data = user_response.json()
    tasks_data = tasks_response.json()

    # Get username from user data
    username = user_data.get("username")

    # Create list of tasks
    tasks = []
    for task in tasks_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks.append(task_dict)

    # Create dictionary with user_id as key and tasks list as value
    data = {user_id: tasks}

    # Set filename to USER_ID.json
    filename = f"{user_id}.json"

    # Write data to file in JSON format
    with open(filename, mode="w") as f:
        json.dump(data, f)

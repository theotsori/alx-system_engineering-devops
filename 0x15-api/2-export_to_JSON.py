#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID,
returns info about their TO DO list progress and exports the data in
JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command line argument
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)
    emp_id = sys.argv[1]

    # Build URLs for user and tasks
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    ts = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)

    # Send requests and get responses
    user_response = requests.get(user_url)
    tasks_response = requests.get(ts)

    # Get JSON data from responses
    user_data = user_response.json()
    tasks_data = tasks_response.json()

    # Get employee name from user data
    employee_name = user_data.get("name")

    # Parse task data to get the num of completed and total num of tasks
    total_tasks = len(tasks_data)
    completed_tasks = sum(1 for task in tasks_data if task['completed'])

    # Create list of tasks
    tasks = []
    for task in tasks_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_data.get("username")
        }
        tasks.append(task_dict)

    # Create dictionary with emp_id as key and tasks list as value
    data = {emp_id: tasks}

    # Set filename to EMPLOYEE_ID.json
    filename = "{}.json".format(emp_id)

    # Write data to file in JSON format
    with open(filename, mode="w") as f:
        json.dump(data, f)

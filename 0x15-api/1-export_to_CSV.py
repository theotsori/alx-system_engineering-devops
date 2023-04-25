#!/usr/bin/python3
"""
Python script that retrieves information about
an employee's TODO list progress from a REST API
and exports the data in CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    # Get user ID from command line argument
    user_id = sys.argv[1]

    # Send GET requests to API to get user and tasks data
    url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    url_tasks = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    user_response = requests.get(url_user)
    tasks_response = requests.get(url_tasks)

    # Parse JSON data
    user = user_response.json()
    tasks = tasks_response.json()
    username = user.get("username")

    # Write data to CSV file
    with open(f"{user_id}.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(
            csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )
        for task in tasks:
            status = "True" if task.get("completed") else "False"
            writer.writerow([user_id, username, status, task.get("title")])

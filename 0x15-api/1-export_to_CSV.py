#!/usr/bin/python3
"""
This script retrieves information about an
employee's TODO list progress from a REST API
and exports the data in CSV format.
"""

import csv
import requests
import sys


def export_todo_list(user_id):
    """
    Retrieve user and tasks data from REST API,
    parse JSON data, and export the data in CSV format.

    Args:
        user_id (int): The ID of the user whose
        TODO list progress will be exported.

    Returns:
        None
    """
    # Send GET requests to API to get user and tasks data
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ks = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    user_response = requests.get(url_user)
    tasks_response = requests.get(ks)

    # Parse JSON data
    user = user_response.json()
    tasks = tasks_response.json()
    username = user.get("username")

    # Write data to CSV file
    with open("{}.csv".format(user_id), mode="w", newline="") as csv_file:
        writer = csv.writer(
            csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )
        for task in tasks:
            status = "True" if task.get("completed") else "False"
            writer.writerow([user_id, username, status, task.get("title")])


if __name__ == "__main__":
    # Get user ID from command line argument
    user_id = sys.argv[1]
    export_todo_list(user_id)

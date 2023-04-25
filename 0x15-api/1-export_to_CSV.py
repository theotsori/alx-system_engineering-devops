#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
and exports the data in CSV format.
"""
import requests
import csv
from sys import argv

if __name__ == "__main__":
    # Get user ID from command line argument
    user_id = argv[1]

    # Send GET requests to API to get user and tasks data
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    url_tasks = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    user_response = requests.get(url_user)
    tasks_response = requests.get(url_tasks)

    # Parse JSON data
    user = user_response.json()
    tasks = tasks_response.json()
    username = user.get('username')

    # Write data to CSV file
    with open('{}.csv'.format(user_id), mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            status = "True" if task.get('completed') else "False"
            writer.writerow([user_id, username, status, task.get('title')])

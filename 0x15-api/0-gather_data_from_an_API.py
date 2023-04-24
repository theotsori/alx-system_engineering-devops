#!/usr/bin/python3
"""
Python script that, using this REST API,for a given employee ID,
returns info about their TO DO list progress
"""
import sys
import requests

if __name__ == "__main__":
    # Get the employee ID from the command line argument
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)
    emp_id = sys.argv[1]

    # Send a GET request to the API to get the employee's todo list
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
    response = requests.get(url)

    # Parse the response to get the num of completed and total num of tasks
    tasks = response.json()
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])

    # Print employee's name, numb of completed tasks, and total num of tasks
    url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    response = requests.get(url)
    employee_name = response.json()['name']
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          completed_tasks,
                                                          total_tasks))

    # Print the titles of completed tasks in the required format
    for task in tasks:
        if task['completed']:
            print("\t {}".format(task['title']))

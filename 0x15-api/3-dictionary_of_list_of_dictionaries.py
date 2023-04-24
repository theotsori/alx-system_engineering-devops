#!/usr/bin/python3
"""
Export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    todo_all_employees = {}

    for user in users:
        user_id = str(user.get('id'))
        todo_all_employees[user_id] = []
        username = user.get('username')

        for todo in todos:
            if user_id == str(todo.get('userId')):
                task = {
                    "username": username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                }
                todo_all_employees[user_id].append(task)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(todo_all_employees, file)

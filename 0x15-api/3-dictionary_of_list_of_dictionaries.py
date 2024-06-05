#!/usr/bin/python3
"""script to export data in the JSON format."""
import json
import requests


def fetch_user_data():
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users').json()
    data_export = {}
    for user in users:
        user_id = user['id']
        user_url = url + f'todos?userld ={user_id}'
        todos = requests.get(user_url).json()
        data_export[user_id] = [
                {
                    'task': todo.get('title'),
                    'completed': todo.get('completed'),
                    'username': user.get('username'),
                }
                for todo in todos
                ]
    return data_export


if __name__ == "__main__":
    data_export = fetch_user_data()
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(data_export, jsonfile, indent=4)

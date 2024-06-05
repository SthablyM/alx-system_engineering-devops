#!/usr/bin/python3
"""script to export data in the CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user_response = requests.get(url + f'users/{user_id}')
    user = user_response.json()
    username = user.get('username')
    todos_response = requests.get(url + 'todos', params={'userId': user_id})
    todos = todos_response.json()
    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for t in todos:
            writer.writerow(
                    [user_id, username, t.get('completed'), t.get('title')])

    print(f"Number of tasks in CSV: {'OK' if len(todos) == \
    len(todos) else 'Incorrect'}")

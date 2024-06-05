#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for t in data2:
        if t.get('id') == int(argv[1]):
            employee = t.get('name')

    for t in data:
        if t.get('userId') == int(argv[1]):
            total += 1

            if t.get('completed') is True:
                completed += 1
                tasks.append(t.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))

    for t in tasks:
        print("\t {}".format(t))

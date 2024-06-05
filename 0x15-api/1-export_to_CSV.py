#!/usr/bin/python3

"""
Python script that exports data in the CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    responses = get('https://jsonplaceholder.typicode.com/users')
    datat = responses.json()

    for t in datat:
        if t['id'] == int(argv[1]):
            employee = t['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)

        for t in data:

            row = []
            if t['userId'] == int(argv[1]):
                row.append(t['userId'])
                row.append(employee)
                row.append(t['completed'])
                row.append(t['title'])

                write.writerow(row)

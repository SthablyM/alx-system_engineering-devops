#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

from requests import get
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    responses = get('https://jsonplaceholder.typicode.com/users')
    datas = responses.json()

    data_export = {}

    for j in datas:

        row = []
        for d in data:

            data_export2 = {}

            if j['id'] == d['userId']:

                data_export2['username'] = j['username']
                data_export2['task'] = d['title']
                data_export2['completed'] = d['completed']
                row.append(data_export2)

        data_export[j['id']] = row

    with open("todo_all_employees.json",  "w") as jfile:

        json_obj = json.dumps(data_export)
        jfile.write(json_obj)

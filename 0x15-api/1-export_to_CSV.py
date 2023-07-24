#!/usr/bin/python3
"""Export data gotten from REST API to CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    idee = sys.argv[1]
    USERNAME = ""
    ENTRY = []
    file_path = idee + ".csv"

    # Retrieving the employee name
    api_url = "https://jsonplaceholder.typicode.com/users/" + idee
    response = requests.get(api_url)
    USERNAME = response.json().get("username")

    # Retrieving the employee completed tasks
    api_url = "https://jsonplaceholder.typicode.com/users/" + idee + "/todos"
    response = requests.get(api_url)

    with open(file_path, 'w') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        # f_writer.delimiter = ','
        # f_writer.quotechar = '"'
        # f_writer.quoting = csv.QUOTE_ALL
        for todo in response.json():
            ENTRY.append(todo.get("userId"))
            ENTRY.append(USERNAME)
            ENTRY.append(todo.get("completed"))
            ENTRY.append(todo.get("title"))
            w.writerow(ENTRY)
            ENTRY = []
    f.close()

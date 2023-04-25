#!/usr/bin/python3
"""Export data gotten from REST API to CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    idee = sys.argv[1]
    NAME = ""
    ENTRY = []
    file_path = idee + ".csv"

    # Retrieving the employee name
    api_url = "https://jsonplaceholder.typicode.com/users/" + idee
    response = requests.get(api_url)
    NAME = response.json().get("name")

    # Retrieving the employee completed tasks
    api_url = "https://jsonplaceholder.typicode.com/users/" + idee + "/todos"
    response = requests.get(api_url)

    with open(file_path, 'w') as f:
        f_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in response.json():
            ENTRY.append(todo.get("userId"))
            ENTRY.append(NAME)
            ENTRY.append(todo.get("completed"))
            ENTRY.append(todo.get("title"))
            f_writer.writerow(ENTRY)
    f.close()

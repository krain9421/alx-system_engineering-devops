#!/usr/bin/python3
"""Script that uses REST API and returns information"""

import requests
import sys

if __name__ == "__main__":
    idee = sys.argv[1]
    NAME = ""
    DONE = 0
    TOTAL = 0
    TITLE = []

    # Retrieving the employee name
    api_url = "https://jsonplaceholder.typicode.com/users/" + idee
    response = requests.get(api_url)
    NAME = response.json().get("name")

    # Retrieving the employee completed tasks
    api_url = "https://jsonplaceholder.typicode.com/users/" + idee + "/todos"
    response = requests.get(api_url)

    for todo in response.json():
        TOTAL += 1
        if todo.get("completed"):
            DONE += 1
            TITLE.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(NAME, DONE, TOTAL))

    # Displaying the completed tasks
    for task in TITLE:
        print("\t {}".format(task))

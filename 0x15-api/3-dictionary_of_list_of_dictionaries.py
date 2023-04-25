#!/usr/bin/python3
"""Export all employee data gotten from REST API to CSV format"""

import json
import requests
import sys

if __name__ == "__main__":
    USERNAME = ""
    file_path = "todo_all_employees.json"
    objects_json = {}

    for idee in range(1, 11):
        # Retrieving the employee name
        api_url = "https://jsonplaceholder.typicode.com/users/" + str(idee)
        response = requests.get(api_url)
        USERNAME = response.json().get("username")

        # Retrieving other employee data
        url = "https://jsonplaceholder.typicode.com/users/"
        api_url = url + str(idee) + "/todos"
        response = requests.get(api_url)

        # with open(file_path, 'w') as f:
        ENTRY = []
        ENTRY_dict = {}
        for todo in response.json():
            # Get the values for the required resources
            userid = todo.get("userid")
            task = todo.get("title")
            completed = todo.get("completed")

            # Store the resource values as a dictionary
            ENTRY_dict.update({"username": USERNAME})
            ENTRY_dict.update({"task": task})
            ENTRY_dict.update({"completed": completed})

            # Append the dictionary to a list
            ENTRY.append(ENTRY_dict)

            # Clear the dictionary
            ENTRY_dict = {}

        objects_json.update({str(idee): ENTRY})

    with open(file_path, 'w') as f:
        json.dump(objects_json, f)
        f.close()
        # json.dump(objects_json, f)

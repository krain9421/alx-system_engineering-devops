#!/usr/bin/python3
"""Export data gotten from REST API to CSV format"""

import json
import requests
import sys

if __name__ == "__main__":
    idee = sys.argv[1]
    USERNAME = ""
    file_path = idee + ".json"

    # Retrieving the employee name
    api_url = "https://jsonplaceholder.typicode.com/users/" + idee
    response = requests.get(api_url)
    USERNAME = response.json().get("username")

    # Retrieving the employee completed tasks
    api_url = "https://jsonplaceholder.typicode.com/users/" + idee + "/todos"
    response = requests.get(api_url)

    with open(file_path, 'w') as f:
        ENTRY = []
        ENTRY_dict = {}
        objects_json = {}
        for todo in response.json():
            # Get the values for the required resources
            userid = todo.get("userid")
            task = todo.get("title")
            completed = todo.get("completed")

            # Store the resource values as a dictionary
            ENTRY_dict.update({"task": task})
            ENTRY_dict.update({"completed": completed})
            ENTRY_dict.update({"username": USERNAME})

            # Append the dictionary to a list
            ENTRY.append(ENTRY_dict)

            # Clear the dictionary
            ENTRY_dict = {}

        objects_json.update({idee: ENTRY})
        json.dump(objects_json, f)
    f.close()

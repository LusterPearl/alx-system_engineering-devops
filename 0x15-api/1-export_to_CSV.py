#!/usr/bin/python3
"""
Fetches information about an employee using a REST API and
exports it to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command line arguments
    user_id = sys.argv[1]

    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user details
    user_response = requests.get(base_url + "users/{}".format(user_id))
    user = user_response.json()
    username = user.get("username")

    # Fetch TODOs for the user
    todos_response = requests.get(
        base_url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    # Write user and TODOs data to a CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write header
        writer.writerow(
                ["User ID", "Username", "Task Completed", "Task Title"])

        # Write data rows
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]

    print("Data exported to {}.csv".format(user_id))

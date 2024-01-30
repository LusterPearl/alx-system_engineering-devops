#!/usr/bin/python3
"""
Ret API to retrieve information about an employee based
on the exports acquired data tto a csv file
"""
import csv
import requests
import sys


if __name__ == "__main__":
    # Obtain the employee ID from the CSV
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write the retrieved data to a CSV file named after the emplyee
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]

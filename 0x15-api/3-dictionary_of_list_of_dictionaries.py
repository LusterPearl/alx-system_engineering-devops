#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv
from os.path import isfile


def read_existing_data(filename):
    if isfile(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(argv) == 2 and argv[1].isdigit():
        employee_id = argv[1]
    else:
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)

    # Construct user URL and fetch employee data from the JSONPlaceholder API
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response_user = requests.get(user_url)
    user_data = response_user.json()
    employee_username = user_data.get("username")

    # Construct todos URL and fetch todos data for the specific employee
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response_todos = requests.get(todos_url)
    todos_data = response_todos.json()

    # Create a dictionary with the required format
    new_employee_data = {employee_id: []}
    for todo in todos_data:
        task_dict = {
            "username": employee_username,
            "task": todo["title"],
            "completed": todo["completed"]
        }
        new_employee_data[employee_id].append(task_dict)

    # Read existing data from the file
    existing_data = read_existing_data("todo_all_employees.json")

    # Update the existing data with the new employee data
    existing_data.update(new_employee_data)

    # Export the updated data to todo_all_employees.json
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=2)

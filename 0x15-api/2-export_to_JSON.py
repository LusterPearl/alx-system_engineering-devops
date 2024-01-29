#!/usr/bin/python3
"""
Script to export data in JSON format based on employee ID.
"""
import requests
import json
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f"Error feteching user data for ID {employee_id})")
        sys.exit(1)

    user_data = user_response.json()

    # Fetch TODOs data
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos"
        f"?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f"Error fetching TODOs data for ID {employee_id}")
        sys.exit(1)

    todos_data = todos_response.json()

    # Filter tasks for this employee
    employee_tasks = [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_data.get("username")
            }
            for task in todos_data
    ]

    # Save data to JSON file
    json_file_path = "todo_all_employees.json"
    with open(json_file_path, mode="a") as json_file:
        json.dump({str(employee_id): employee_tasks}, json_file)

    print(f"Data for employee ID {employee_id} "
          f"exported to todo_all_employees.json")

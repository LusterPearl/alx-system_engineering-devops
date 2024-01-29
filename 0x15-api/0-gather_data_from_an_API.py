#!/usr/bin/python3
"""
Script to gather data from an API based on employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODOs data
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos"
        f"?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]

    # Display information
    employee_name = user_data.get('name')
    num_done_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks"
          f"({num_done_tasks}/{total_tasks}):"
          )

    # Display completed tasks titles
    for task in completed_tasks:
        print(f"\t {task['title']}")

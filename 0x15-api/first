#!/usr/bin/python3
"""
Script to export data in CSV format based on employee ID.
"""
import requests
import csv
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f"Error fetching user data for ID {employee_id}")
        sys.exit(1)

    user_data = user_response.json()

    # Fetch TODOs data
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter tasks for this employee
    user_id = user_data.get("id")
    username = user_data.get("username")

    # Corrected formatting for user ID and username
    print(f"User ID: {user_id} / Username: {username}")

    employee_tasks = [
        {
            "USER_ID": user_id,
            "USERNAME": username,
            "TASK_COMPLETED_STATUS": str(task.get("completed")),
            "TASK_TITLE": task.get("title")
        }
        for task in todos_data
    ]

    # Save data to CSV file
    csv_file_path = f"{employee_id}.csv"
    with open(csv_file_path, mode="w", newline="") as csv_file:
        fieldnames = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write tasks data
        writer.writerows(employee_tasks)

    print(f"Data exported to {csv_file_path}")

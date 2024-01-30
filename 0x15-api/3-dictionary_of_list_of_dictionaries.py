#!/usr/bin/python3
"""
Retrieves data from an API and exports it to a JSON file
"""
import json
import requests

API_URL = 'https://jsonplaceholder.typicode.com'
"""The URL of the JSONPlaceholder """


if __name__ == '__main__':
    # Retrieve users data using API
    users_res = requests.get('{}/users'.format(API_URL)).json()
    # Retrieve todos data using API
    todos_res = requests.get('{}/todos'.format(API_URL)).json()
    # Start a dictionary to store users' data
    users_data = {}

    # Go through each user
    for user in users_res:
        # Collect a user ID and username
        user_id = user.get('id')
        user_name = user.get('username')
        # Filter todos associated with the user
        user_todos = list(filter(lambda x: x.get('userId') == user_id,
                                 todos_res))
        # Start user data
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            user_todos
        ))
        # Store data in the dictionary
        users_data['{}'.format(user_id)] = user_data

    # Write the JSON data to a file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(users_data, json_file)

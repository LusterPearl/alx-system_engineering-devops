#!/usr/bin/python3
'''A script that retrieves data from an API and exports it to a JSON file.'''
import json
import requests

API_URL = 'https://jsonplaceholder.typicode.com'
"""The base URL of the JSONPlaceholder API."""

if __name__ == '__main__':
    # Make an API call to retrieve users' data
    users_res = requests.get('{}/users'.format(API_URL)).json()
    # Make an API call to retrieve todos' data
    todos_res = requests.get('{}/todos'.format(API_URL)).json()
    # Initialize a dictionary to store users' data
    users_data = {}

    # Iterate through each user
    for user in users_res:
        # Extract user ID and username
        user_id = user.get('id')
        user_name = user.get('username')
        # Filter todos associated with the user
        user_todos = list(filter(lambda x: x.get('userId') == user_id, todos_res))
        # Prepare user's data
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            user_todos
        ))
        # Store user's data in the dictionary
        users_data['{}'.format(user_id)] = user_data

    # Write the JSON data to a file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(users_data, json_file)

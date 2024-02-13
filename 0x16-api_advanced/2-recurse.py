#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    If no results are found for the given subreddit, returns None.
    """
    if hot_list is None:
        hot_list = []

    base_url = "https://www.reddit.com/r/"
    url = f"{base_url}{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/1.0'}

    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"HTTP error occurred: {response.status_code}")
        return None

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title']
        hot_list.append(title)

    after = data['data'].get('after')
    if after:
        recurse(subreddit, hot_list, after)

    return hot_list


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")

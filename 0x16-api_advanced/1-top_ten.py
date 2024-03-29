#!/usr/bin/python3
"""
1-top_ten
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    elif response.status_code == 302:
        print("None")
    else:
        print("None")


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    top_ten(subreddit)

#!/usr/bin/python3
"""
Module to interact with Reddit's API
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): The 'after' parameter for pagination.
        word_count (dict): Dictionary to store word counts.

    Returns:
        None
    """
    if word_count is None:
        word_count = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'bhalut'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                word_count[word] = word_count.get(
                                    word, 0) + title.count(word.lower())

        after = data['after']
        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_count:
                if count > 0:
                    print(f"{word}: {count}")

    else:
        print(f"Failed to fetch data for subreddit '{subreddit}':"
              f"{response.status_code}")

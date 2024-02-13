#!/usr/bin/python3
"""
100-count
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    base_url = "https://www.reddit.com/r/"
    url = f"{base_url}{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/1.0'}

    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        if response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print("HTTP error occured:", response.status_code)
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title']
        for word in word_list:
            if word.lower() in title.lower().split():
                word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

    after = data['data'].get('after')
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        print_results(word_count)


def print_results(word_count):
    """
    Prints the sorted count of keywords in descending order.
    If counts are the same, keywords are sorted alphabetically.
    """
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    keywords = input("Enter list of keywords separated by spaces: ").split()
    count_words(subreddit, keywords)

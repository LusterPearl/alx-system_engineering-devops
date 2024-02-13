#!/usr/bin/python3
"""
2-recurse retriei functions
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    If no results are found for the given
    """
    headers = {'User-Agent': 'reddit-recursive-fetch'}
    params = {'limit': 100, 'after': after}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            children = data['data']['children']
            for child in children:
                hot_list.append(child['data']['title'])
            after = data['data']['after']
            if after is not None:
                count_words(subreddit, word_list, hot_list, after)
        count_occurrences(hot_list, word_list)
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
    else:
        print("Error occurred while fetching data:", response.status_code)


def count_occurrences(hot_list, word_list):
    """
    Counts occurrences of keywords in the hot articles.

    Args:
        hot_list (list): List of hot article titles.
        word_list (list): List of keywords to count.

    Returns:
        None
    """
    keyword_count = {}
    for title in hot_list:
        for word in word_list:
            if word.lower() in title.lower().split():
                keyword_count[word.lower()] = keyword_count.get(
                        word.lower(), 0) + 1

    sorted_counts = sorted(keyword_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")


if __name__ == '__main__':
    subreddit = input("Enter the subreddit name: ")
    keywords = input("Enter the keywords separated by spaces: ").split()
    count_words(subreddit, keywords)

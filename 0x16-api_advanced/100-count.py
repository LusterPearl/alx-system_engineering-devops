#!/usr/bin/python3
"""
100-count aicles
"""

import requests
import json


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if count is None:
        count = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'bhalut'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                count[word] = count.get(word, 0) + title.count(word.lower())

        after = data['after']
        if after:
            count_words(subreddit, word_list, after, count)
        else:
            sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
            for word, word_count in sorted_count:
                if word_count > 0:
                    print(f"{word}: {word_count}")

    else:
        print(f"Failed to fetch data for subreddit '{subreddit}':
              {response.status_code}")

#!/usr/bin/python3
"""
 Recursively fetches all hot articles
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Recursively fetch the top post titles from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the top post titles.
        after (str): The 'after' parameter for pagination.
        limit (int): The maximum number of posts to fetch.

    Returns:
        list: The list of top post titles from the subreddit.
    """
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)

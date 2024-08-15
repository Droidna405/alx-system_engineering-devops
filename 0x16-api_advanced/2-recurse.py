#!/usr/bin/python3
"""
This module defines the recursive function `recurse`
that queries the Reddit API to return a list of all hot article titles
for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursive function to get all hot articles' titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles of hot articles.

    Returns:
        list: A list of titles of all hot articles, or None if the
    subreddit is invalid.
    """
    # Define the URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Define headers including User-Agent
    headers = {"User-Agent": "JmRedditBot/0.3"}

    # Send the GET request to Reddit
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        # Add titles to the hot_list
        for post in posts:
            hot_list.append(post['data']['title'])

        # Check if there is more data to fetch
        after = data['data'].get('after')
        if after:
            # Recursive call with the new 'after' parameter
            recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        # If there was an error, return None
        return None

    return hot_list

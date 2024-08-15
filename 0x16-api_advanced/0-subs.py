#!/usr/bin/python3
"""
This module defines 'number_of_subscribers' that queries the
REDDIT API and returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    function should get the number of subscribers in a subreddit
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: The number of subscribers, or 0 if the subreddit
             doesn't exist.
    """
    headers = {"User-Agent": "JmRedditSubBot/0.1"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    subs = response.json().get("data").get("subscribers")
    return subs

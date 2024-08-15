#!/usr/bin/python3
"""
This module defines the recursive function `count_words`
that queries the Reddit API to count the occurrences of given keywords
in the titles of all hot articles for a given subreddit.
"""

import re
import requests
from collections import defaultdict

def count_words(subreddit, word_list):
    """
    Recursive function to count occurrences of given keywords in the titles
    of all hot articles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): The list of keywords to count.

    Returns:
        None: Prints the counts of each keyword sorted by count and alphabetically.
    """
    def fetch_hot_articles(subreddit, after=None):
        """
        Helper function to fetch hot articles recursively.

        Args:
            subreddit (str): The name of the subreddit.
            after (str): The 'after' parameter for pagination.

        Returns:
            tuple: A tuple containing the list of titles and the 'after' parameter for next page.
        """
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {"User-Agent": "MyRedditBot/0.1"}
        params = {"after": after} if after else {}

        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            titles = [post['data']['title'] for post in data['data']['children']]
            after = data['data'].get('after')
            return titles, after
        else:
            return [], None

    def count_titles(titles, keywords, counts):
        """
        Helper function to count occurrences of keywords in titles.

        Args:
            titles (list): The list of titles.
            keywords (list): The list of keywords to count.
            counts (dict): Dictionary to store counts of each keyword.

        Returns:
            None: Updates the counts dictionary.
        """
        keyword_patterns = {keyword.lower():
                            re.compile(r'\b' + re.escape(keyword.lower()) + r'\b') for keyword in keywords}
        
        for title in titles:
            title_lower = title.lower()
            for keyword, pattern in keyword_patterns.items():
                counts[keyword] += len(pattern.findall(title_lower))

    # Recursive function to get all titles
    def recurse(subreddit, word_list, counts, after=None):
        titles, new_after = fetch_hot_articles(subreddit, after)
        if titles:
            count_titles(titles, word_list, counts)
            if new_after:
                recurse(subreddit, word_list, counts, new_after)
        else:
            # Print results sorted by count (desc) and alphabetically
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                if count > 0:
                    print(f"{keyword}: {count}")

    # Initialize counts dictionary and start recursion
    counts = defaultdict(int)
    recurse(subreddit, word_list, counts)

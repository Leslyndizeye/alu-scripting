#!/usr/bin/python3
"""
Recursive function to retrieve titles of all hot articles from a given subreddit using Reddit API.
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetches titles of all hot articles from a subreddit.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): A list to accumulate hot article titles.
        after (str): The 'after' parameter for pagination.

    Returns:
        list or None: A list containing the titles of all hot articles, or None if subreddit is invalid or no results found.
    """

    # Base case: if hot_list is None, initialize it
    if hot_list is None:
        hot_list = []

    # Set a custom User-Agent header to avoid any API request issues
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    # Construct the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Add 'after' parameter for pagination if it's not None
    params = {'limit': 100}
    if after:
        params['after'] = after

    # Send a GET request to the API
    response = requests.get(url, headers=headers, params=params)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse JSON data from the response
        data = response.json()

        # Extract titles from the response and append them to hot_list
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])

        # If there are more pages, recursively call recurse with the 'after' parameter
        if data['data']['after']:
            return recurse(subreddit, hot_list, data['data']['after'])
        else:
            # If no more pages, return the accumulated hot_list
            return hot_list
    else:
        # If the subreddit is invalid or there's an issue with the request, return None
        return None

# Example usage:
# subreddit = 'python'
# hot_articles = recurse(subreddit)
# print(hot_articles)

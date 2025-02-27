#!/usr/bin/python3
"""
Module for querying the Reddit API and returning the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a
    given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is invalid.
    """
    # Set up the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/your_username)'
    }

    try:
        # Make the request, setting allow_redirects to False to handle invalid subreddits
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and return the number of subscribers
            data = response.json()
            return data['data']['subscribers']
        else:
            # If not successful (404 or other error), return 0
            return 0
    except Exception:
        # Handle any exceptions that might occur during the request
        return 0
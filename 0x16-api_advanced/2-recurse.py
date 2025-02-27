#!/usr/bin/python3
"""
Module for querying the Reddit API recursively and returning titles of all hot
articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): List to accumulate post titles. 
                                  Defaults to None.
        after (str, optional): Token for pagination. Defaults to None.

    Returns:
        list: List of all hot article titles, or None if the subreddit is 
              invalid or no results are found.
    """
    # Initialize hot_list if None
    if hot_list is None:
        hot_list = []

    # Set base URL for the Reddit API
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Add limit parameter and after parameter if it exists
    params = {'limit': 100}  # Get maximum (100) results per request
    if after:
        params['after'] = after

    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/your_username)'
    }

    try:
        # Make the request, setting allow_redirects to False to handle invalid subreddits
        response = requests.get(
            base_url, 
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            posts = data['data']['children']

            # If no posts were found
            if not posts:
                return hot_list if hot_list else None

            # Add titles to the hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # Check if there are more pages (pagination)
            after = data['data']['after']
            if after:
                # Recursively call the function with the new after value
                return recurse(subreddit, hot_list, after)
            else:
                # No more pages, return the complete list
                return hot_list
        else:
            # If not successful (404 or other error), return None
            return None
    except Exception:
        # Handle any exceptions that might occur during the request
        return None
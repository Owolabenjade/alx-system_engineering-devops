#!/usr/bin/python3
"""
Module for querying the Reddit API and printing the titles of the first 10 hot
posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: This function doesn't return anything, it prints the titles or None.
    """
    # Set up the URL for the Reddit API with limit=10 to get the top 10 posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/your_username)'
    }

    try:
        # Make the request, setting allow_redirects to False to handle invalid subreddits
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            posts = data['data']['children']
            
            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post['data']['title'])
        else:
            # If not successful (404 or other error), print None
            print(None)
    except Exception:
        # Handle any exceptions that might occur during the request
        print(None)
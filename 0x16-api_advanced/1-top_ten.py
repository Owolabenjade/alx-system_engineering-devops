#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    # Reddit API URL for getting hot posts from a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Custom User-Agent to avoid "Too Many Requests" errors
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/alx_student)"
    }

    # Make the request to the Reddit API
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Get the list of posts
            posts = data.get("data", {}).get("children", [])
            
            # Print the title of each post
            for post in posts:
                print(post.get("data", {}).get("title", ""))
        else:
            # If the subreddit is invalid or not found, print None
            print(None)
    except requests.exceptions.RequestException:
        # Handle any request exceptions
        print(None)

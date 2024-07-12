#!/usr/bin/python3
"""Query the Reddit API & return no. of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number
    of subscribers for a given subreddit.

    :param subreddit: string, the name of the subreddit to query
    :return: int, the number of subscribers (0 if invalid subreddit)
    """
    # Set up the API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "MyBot/1.0 (by /u/YourRedditUsername)"
    }

    try:
        # Send GET request to the API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # If not successful (including redirects), return 0
            return 0
    except:
        # If any error occurs during the request, return 0
        return 0

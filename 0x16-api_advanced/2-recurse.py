#!/usr/bin/python3
"""
Reddit API query to get the titles of all hot posts
for a given subreddit using recursion.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list
    containing the titles of all hot articles
    for a given subreddit. If no results are found for
    the given subreddit, it returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-user-agent'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers,
                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            articles = data['data']['children']
            if not articles:
                return hot_list if hot_list else None

            for article in articles:
                hot_list.append(article['data']['title'])

            after = data['data']['after']
            if after is None:
                return hot_list
            return recurse(subreddit, hot_list, after)
        else:
            return None
    except requests.RequestException:
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")

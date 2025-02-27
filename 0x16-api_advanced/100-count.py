#!/usr/bin/python3
"""
Module for querying the Reddit API, parsing the titles of hot articles,
and printing a sorted count of given keywords.
"""
import re
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count.
        after (str, optional): Token for pagination. Defaults to None.
        word_counts (dict, optional): Dictionary to track word counts.
                                     Defaults to None.

    Returns:
        None: This function prints the results instead of returning them.
    """
    # Initialize word_counts dictionary if None
    if word_counts is None:
        # Create a case-insensitive dictionary of words
        word_counts = {}
        for word in word_list:
            # Convert to lowercase for case-insensitivity
            word_lower = word.lower()
            # Add to dictionary or increment if already exists
            if word_lower in word_counts:
                word_counts[word_lower] += 1
            else:
                word_counts[word_lower] = 1

        # Reset all counts to 0 (we're using the dict keys for unique words)
        for word in word_counts:
            word_counts[word] = 0

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

            # Process each post title
            for post in posts:
                title = post['data']['title'].lower()
                # Split the title into words and count occurrences
                for word in word_counts:
                    # Use regex to find whole word matches only
                    # This avoids matching 'java' in 'javascript' or 'java.' etc.
                    matches = re.findall(r'\b{}\b'.format(word), title)
                    word_counts[word] += len(matches)

            # Check if there are more pages (pagination)
            after = data['data']['after']
            if after:
                # Recursively call the function with the new after value
                return count_words(subreddit, word_list, after, word_counts)
            else:
                # No more pages, print the results
                print_results(word_counts)
        else:
            # If not successful, print nothing (as per requirements)
            return
    except Exception:
        # Handle any exceptions, print nothing (as per requirements)
        return


def print_results(word_counts):
    """
    Prints the results in the required format.

    Args:
        word_counts (dict): Dictionary with words and their counts.
    """
    # Create a list of (word, count) tuples, ignoring words with count 0
    results = [(word, count) for word, count in word_counts.items() if count > 0]
    
    # Sort results by count (descending) and then by word (ascending)
    results.sort(key=lambda x: (-x[1], x[0]))
    
    # Print results
    for word, count in results:
        print(f"{word}: {count}")
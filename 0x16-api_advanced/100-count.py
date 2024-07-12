#!/usr/bin/python3
"""
Reddit API query to count keyword occurrences in titles of hot posts for
a given subreddit using recursion.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).

    :param subreddit: Subreddit name to query
    :param word_list: List of keywords to count
    :param after: Used for pagination (default: None)
    :param word_count: Dictionary to hold the
    count of words (default: empty)
    """
    if after is None:
        word_list = [word.lower() for word in word_list]
        word_count = {word: 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/1.0'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            articles = data['data']['children']
            for article in articles:
                title = article['data']['title'].lower().split()
                for word in word_list:
                    word_count[word] += title.count(word)

            after = data['data']['after']
            if after is None:
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    if count > 0:
                        print(f"{word}: {count}")
                return
            return count_words(subreddit, word_list, after, word_count)
        else:
            return
    except requests.RequestException:
        return


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

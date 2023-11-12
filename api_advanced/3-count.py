#!/usr/bin/python3
"""
recursive funtion that
parses the titles of all hot posts
and prints out a sorted count of given words
"""


import json
import requests
import sys


def count_words(subreddit, word_list, after=None, results=None):
    """
    recursive function
    """
    if results is None:
        results = {}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 10, 'after': after} if after else {'limit': 10}
    headers = {
            "User-Agent": "3-count/1.0"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Error: HTTP Status Code {response.status_code}")
        return

    data = response.json()

    if 'data' in data and 'children' in data['data']:
        for child in data['data']['children']:
            title_words = child['data']['title'].lower().split()

            for word in word_list:
                if word.lower() in title_words:
                    results[word.lower()] = results.get(word.lower(), 0) + title_words.count(word.lower())

        count_words(subreddit, word_list, after=data['data'].get('after'), results=results)

       
    else:
        print("Error: Unexpected response format")

                                                                                                                                                                                if results:
        sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_results:
            print(f"{word}: {count}")


if __name__ == '__main__':
    pass

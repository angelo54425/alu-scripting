#!/usr/bin/python3
"""top ten"""
import requests


def top_ten(subreddit):
    """a function that prints the titles of the first 10 hot posts"""
    headers = {'User-Agent': 'My API advanced 1.0'}
    url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        for i in range(10):
            print(
                    json_data.get('data')
                    .get('children')[i]
                    .get('data')
                    .get('title')
                )
    else:
        print(None)

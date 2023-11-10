#!/usr/bin/python3
"""
2-main
"""

import json
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """get all hot post titles for a subreddit recursively"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {}
    if after:
        params['after'] = after
    result = requests.get(url, headers=headers,
                          params=params, allow_redirects=False)
    if result.status_code != 200:
        return None
    body = result.json()
    children = body['data']['children']
    for child in children:
        hot_list.append(child['data']['title'])
    if not body['data']['after']:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after=body['data']['after'])

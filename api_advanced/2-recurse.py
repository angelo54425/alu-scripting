#!/usr/bin/python3
"""
recursive function that
returns a list containing
titles of all hot articles
"""


import json
import requests
import sys


def recurse(subreddit, hot_list=None, after=None):
    """
    recursive function
    """
    if hot_list is None:
        hot_list = []

    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            "User-Agent": "2-recurse/1.0"
    }
    params = {"after": after} if after else{}
    response = requests.get(URL, headers=headers, params=params)

    if (response.status_code) == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])

        for child in children:
            title = child.get("data", {}).get("title")
            if title:
                hot_list.append(title)

                after = data.get("after")

                if after:
                    recurse(subreddit, hot_list, after)

                else:
                    return hot_list

            else:
                return ('None')

    else:
        return None

if __name__ == "__main__":
    pass

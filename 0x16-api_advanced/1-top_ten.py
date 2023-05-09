#!/usr/bin/python3
"""A function that queries and prints the titles of the
first 10 hot posts for a given subreddit"""

import requests


def top_ten(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    apiUrl = "https://reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Google Chrome Version 113.0.5672.93"
    limits = 10

    response = requests.get(
        apiUrl, headers={"user-agent": userAgent}, params={"limit": limits})
    if not response:
        print('None')
        return
    response = response.json()
    list_obj = response['data']['children']
    for obj in list_obj:
        print(obj['data']['title'])
    return

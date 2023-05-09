#!/usr/bin/python3
"""A function that queries and returns the number of
subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    apiUrl = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "Google Chrome Version 113.0.5672.93"

    response = requests.get(apiUrl, headers={"user-agent": userAgent})
    if not response:
        return 0
    retValue = response.json().get('data').get('subscribers')
    if retValue:
        return retValue
    else:
        return 0

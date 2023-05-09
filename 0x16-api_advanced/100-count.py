#!/usr/bin/python3
"""A module containing functions for working with the Reddit API."""
import requests


def count_words(subreddit, word_list, count_dict={}, after=None):
    """Counts the number of times each word in a given wordlist
    occurs in a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    params = {"limit": 50}
    if after:
        params["after"] = after
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={
            "User-Agent": "Google Chrome Version 113.0.5672.93"},
        params=params,
        allow_redirects=False)
    if req.status_code == 200:
        posts = req.json().get("data").get("children")
        for post in posts:
            title = post.get("data").get("title")
            word_list = [word.lower() for word in word_list]
            for word in word_list:
                w_count = title.split().count(word)
                if count_dict.get(word):
                    count_dict[word] += w_count
                else:
                    count_dict[word] = w_count
        if req.json().get("data").get("after"):
            count_words(
                subreddit,
                word_list=word_list,
                count_dict=count_dict,
                after=req.json().get("data").get("after"))
        else:
            for pair in sorted(
                    count_dict.items(),
                    key=lambda kv: (
                        kv[1],
                        kv[0]),
                    reverse=True):
                if pair[1]:
                    print("{}: {}".format(pair[0].strip(), pair[1]))

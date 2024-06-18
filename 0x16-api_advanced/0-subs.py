#!/usr/bin/python3
"""
function that queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    url = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if url.status_code == 200:
        return url.json().get("data").get("subscribers")
    else:
        return 0

#!/usr/bin/python3
"""
function that queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "My_User-Agent"},
    )

    if url.status_code == 200:
        return url.json().get("data").get("subscribers")
    else:
        return 0

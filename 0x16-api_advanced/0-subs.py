#!/usr/bin/python3
"""
 function that queries the Reddit API and returns the number of
 subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of total subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    sub_acout = response.json().get("data")
    return sub_acount.get("subscribers")

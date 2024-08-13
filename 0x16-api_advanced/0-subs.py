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
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 403:
        return 0
    data = response.json().get("data")
    if data:
        return data.get("subscribers", 0)
    else:
        return 0


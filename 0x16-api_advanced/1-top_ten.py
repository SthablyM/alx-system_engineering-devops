#!/usr/bin/python3
"""
Function that Queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit=10'.format(
        subreddit)
    headers = {'User-Agent': 'my-reddit-app/1.0 (by /u/SthablyM)'}
    response = requests.get(url, headers=headers)
    try:
        results = response.json()['data']['children']
        for c in results:
            print(c['data']['title'])
    except KeyError:
        print("None")

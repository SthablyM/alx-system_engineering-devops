#!/usr/bin/python3
"""
 function that queries the Reddit API and returns the number of
 subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of total subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

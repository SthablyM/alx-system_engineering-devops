#!/usr/bin/python3
"""
 function that queries the Reddit API and returns the number of
 subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of total subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'my-reddit-app/1.0 (by /u/SthablyM)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(response)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0 
    except requests.RequestException:
        return 0

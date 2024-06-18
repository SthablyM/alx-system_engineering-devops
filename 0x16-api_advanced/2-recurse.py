#!/usr/bin/python3
""" recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:recurse:v1.0 (by /u/yourusername)'}
    params = {'limit': 100, 'after': after}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

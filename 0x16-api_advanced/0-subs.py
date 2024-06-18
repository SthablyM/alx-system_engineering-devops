#!/usr/bin/python3
""" function that queries the Reddit  API"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyRedditBot/0.1)'} 
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 400:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

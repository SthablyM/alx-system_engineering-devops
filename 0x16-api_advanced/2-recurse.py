#!/usr/bin/python3
""" 
recursive function that queries the Reddit API and returns a
list containing
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """Recursively retrieves hot articles from a subreddit."""
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'your-app-name/v1.0 (by /u/your-username)'
    }
    
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        print("Error: Unable to fetch data.")
        return None

    try:
        data = response.json().get('data', {})
        children = data.get('children', [])

        for child in children:
            hot_list.append(child['data']['title'])

        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
    except Exception as e:
        print(f"Error: {e}")
        return None

    return hot_list

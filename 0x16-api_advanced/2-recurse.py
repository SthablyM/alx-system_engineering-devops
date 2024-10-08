#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=''):
    """
    Queries the Reddit API and returns a list containing the titles of all hot
    articles for a given subreddit.
    """
    base = 'https://www.reddit.com/'
    endpoint = 'r/{}/hot.json'.format(subreddit)
    query_string = '?show="all"&limit=100&after={}&count={}'.format(
        after, count)
    url = base + endpoint + query_string
    headers = {'User-Agent': 'your-app-name/v1.0 (by /u/SthablyM'}
    response = requests.get(url, headers=headers)
    if not response.ok:
        if len(hot_list) == 0:
            return None
        else:
            return hot_list

    data = response.json()['data']
    for child in data['children']:
        hot_list.append(child['data']['title'])
    after = data['after']
    dist = data['dist']
    if (after):
        recurse(subreddit, hot_list, count + dist, after)

    if len(hot_list) == 0:
        return None
    else:
        return hot_list

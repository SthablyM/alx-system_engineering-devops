#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, hot_list=[], viewed_count=0, after=''):
    """
    Queries the Reddit API, parses the title of all hot articles, and prints a
    sorted count of given keywords.
    """
    base = 'https://www.reddit.com/'
    endpoint = 'r/{}/hot.json'.format(subreddit)
    query_string = '?show="all"&limit=100&after={}&count={}'.format(
        after, viewed_count)
    url = base + endpoint + query_string
    headers = {'User-Agent': 'my-reddit-app/1.0 (by /u/SthablyM'}
    response = requests.get(url, headers=headers)
    if not response.ok:
        return

    data = response.json()['data']
    for child in data['children']:
        hot_list.append(child['data']['title'])
    after = data['after']
    dist = data['dist']
    if (after):
        count_words(subreddit, [], hot_list, viewed_count + dist, after)

    if viewed_count == 0:
        result = {}
        hot_list = [word.lower() for w in hot_list]
        count_words = ' '.join(hot_list).lower().split(' ')
        for k in count_words:
            for search_word in hot_list:
                if k == search_word:
                    result.setdefault(search_word, 0)
                    result[search_word] += 1

        for c, count in sorted(
            sorted(result.items()), key=lambda x: x[1], reverse=True
        ):
            print("{}: {}".format(c, count))

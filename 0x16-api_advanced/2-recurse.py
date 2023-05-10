#!/usr/bin/python3
"""Script that queries the Reddit API and returns a list
    containing the titles of all hot articles for a subreddit
"""

import requests


def recurse(subreddit, hot_list=[]):
    """Function returns a list containing titles
        of all hot articles for `subreddit`
    """
    api_url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(api_url, headers=headers)

    # Check if the subreddit is valid
    if response.status_code == 404:
        return None

    for item in response.json().get('data').get('children'):
        hot_list.append(item['data']['title'])

    after = response.json().get('data').get('after')
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list=hot_list)

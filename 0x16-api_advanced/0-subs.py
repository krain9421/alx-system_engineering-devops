#!/usr/bin/python3
"""Script that queries the Reddit API and returns the number of subscribers
    for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Function returns the number of subscribers
        for a given subreddit
    """
    api_url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(api_url, headers=headers)

    # Check if the subreddit is valid
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0

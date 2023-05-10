#!/usr/bin/python3
"""Script that queries the Reddit API and prints the tiles of the first
    10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Function returns the first 10 host posts listed
        for `subreddit`
    """
    api_url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(api_url, headers=headers)

    # Check if the subreddit is valid
    if response.status_code == 200:
        # Print the first 10 hot posts
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)

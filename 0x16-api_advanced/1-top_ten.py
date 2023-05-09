#!/usr/bin/python3
"""
Function that queries the Rddit api and
prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for post in data:
            print(post["data"]["title"])
    else:
        print(None)

#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursive function"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url,
                            headers=headers,
                            params={"limit": 100, "after": after})
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for post in data:
            hot_list.append(post["data"]["title"])
        after = response.json()["data"]["after"]
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after=after)
    else:
        return None

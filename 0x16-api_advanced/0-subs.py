#!/usr/bin/python3
"""
Function that queries reddit api
and returns no. of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the reddit api and returns the number odf subs
    Args:
        subreddit: The name of the subreddit.
    Returns:
        The number of subscribers for the subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

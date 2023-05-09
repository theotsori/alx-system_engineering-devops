#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces. Javascript should count as javascript,
    but java should not).

    Args:
      subreddit: The name of the subreddit.
      word_list: A list of keywords.

    Returns:
      A list of tuples containing the keyword and the count of occurrences.
    """
    if counts is None:
        counts = {}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    for child in data['data']['children']:
        title = child['data']['title'].lower()
        for word in word_list:
            if ' '+word.lower()+' ' in title:
                if word.lower() in counts:
                    counts[word.lower()] += 1
                else:
                    counts[word.lower()] = 1
    if data['data']['after'] is not None:
        return count_words(subreddit,
                           word_list,
                           after=data['data']['after'],
                           counts=counts)
    else:
        items = [(k, v) for k, v in counts.items() if v > 0]
        items.sort(key=lambda x: (-x[1], x[0]))
        for k, v in items:
            print("{}: {}".format(k, v))

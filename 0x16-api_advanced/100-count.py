#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""
import requests


def count_words(subreddit, word_list, after='', counts={}):
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
    if not word_list:
        return
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 100, 'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    data = response.json()['data']
    children = data['children']
    after = data['after']
    
    for post in children:
        title = post['data']['title'].lower()
        for word in word_list:
            if ' ' + word.lower() + ' ' in title:
                if word.lower() not in counts:
                    counts[word.lower()] = 1
                else:
                    counts[word.lower()] += 1
    
    if after is not None:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print('{}: {}'.format(word, count))

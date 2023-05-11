#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""
import requests


def count_words(subreddit, word_list, after='', word_count={}):
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
    if after is None:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, params=params)

    response.raise_for_status()

    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        title = post["data"]["title"]
        for word in word_list:
            if word.lower() in title.lower() and not any(
                prefix in title.lower() for prefix in ["java.", "java!", "java_"]
            ):
                word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

    count_words(subreddit, word_list, data["data"]["after"], word_count)

#!/usr/bin/python3
import requests
"""
Recursive function that queries a Reddit API
"""


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursive function that queries the Reddit API,
    parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    if counts is None:
        counts = {}

    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)

    headers = {'User-Agent': 'Custom User Agent by u/ResponsibleCup1157 for holberton'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP error
        data = response.json().get('data')

        if data:
            children = data.get('children')
            if children:
                for post in children:
                    title = post['data']['title']
                    for word in word_list:
                        word_lower = word.lower()
                        if word_lower in title.lower():
                            counts[word_lower] = counts.get(word_lower, 0) + 1
        after = data.get('after') if data else None
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch data from Reddit: {}".format(e))
        return None
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))
        return None

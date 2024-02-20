#!/usr/bin/python3
"""
A function that queries the Reddit API
Prints the titles of the first 10 hot posts
Returns None: on invalid subbreddit
Returns 1: as ValueError code
Returns ok: on matching Status Code

"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests
    import sys


    sub_info = requests.get("https://www.reddit.com/r/{}.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    """Debugging"""
    print("Status Code:", sub_info.status_code)

    if sub_info.status_code >= 300:
        print("Invalid Status Code")
        return None
    
    try:
        for child in sub_info.json().get("data").get("children")[:10]:
            print(child.get("data").get("title"))
    except ValueError:
        return 1

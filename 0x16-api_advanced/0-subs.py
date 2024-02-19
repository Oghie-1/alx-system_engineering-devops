#!/usr/bin/python3
"""A function that queries the Reddit API
returns the number of subscribers for a given subreddit
arg is invalid, return 0"""


def number_of_subscribers(subreddit):
    """Queries the reddit api and returns the number of subscribers
    to the subreddit"""

    import requests

    sub_info = requests.get("https://www.redit.com/r/{}.json".format(subreddit),
            headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False)
    
    #debugging
    print("Status Code:", sub_info.status_code)

    if sub_info.status_code >= 300:
        print("Ok")
        try:
            return sub_info.json().get("data").get("listing")
        except ValueError:
            return 1

    return 0

#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of subscribers for a given subreddit
arg is invalid
return 0"""


def number_of_subscribers(subreddit):
    """Queries the reddit api and returns the number of subscribers
    to the subreddit"""

    import requests


    sub_info = requests.get("https://www.redit.com/r/{}/about.json".format(subreddit), headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False)

    print("Status Code:", sub_info.status_code) #debugging 

    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")

#!/usr/bin/python3
"""
Importing requests module
"""
import requests
from requests import get

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit. Returns 0 if subreddit is None or not a string,
             or if an error occurs during the API request.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = get(url, headers=user_agent)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        all_data = response.json()
        return all_data.get('data').get('subscribers')
    except Exception as e:
        print("An error occurred:", e)
        return 0

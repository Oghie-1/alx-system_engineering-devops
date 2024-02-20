#!/usr/bin/python3
"""
Recursively queries the Reddit API
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """Recursively queries the Reddit API and 
    returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the titles of hot articles. 
        Defaults to None.
        after (str, optional): Identifier for the last post in the previous 
        page of results. Defaults to None.

    Returns:
        list: List containing the titles of all 
        hot articles for the given subreddit.
        Returns None if no results are found or if the subreddit is not valid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100}  # Get 100 posts per request
    if after:
        params["after"] = after

    try:
        response = requests.get(url, params=params, 
                headers={"User-Agent": "My-User-Agent"})
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        data = response.json()["data"]
        children = data["children"]
        after = data["after"]

        for child in children:
            hot_list.append(child["data"]["title"])

        # Recursively call the function with the updated 'after' parameter
        if after:
            recurse(subreddit, hot_list, after)

        return hot_list

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"The subreddit '{subreddit}' does not exist.")
        else:
            print("HTTP error occurred:", http_err)
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

#!/usr/bin/python3
import json
import sys
import requests


def number_of_subscribers(subreddit):
	"""
	Function that queries the Reddit API and returns the number of subscribers.
	If the subreddit is invalid or any other error occurs, returns 0.
	"""

	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {'User-Agent': 'Custom User Agent by /u/ResponsibleCup1157 for Holberton School'}

	try:
		response = requests.get(url, headers=headers, allow_redirects=False)
		
		if response.status_code < 300:
			data = response.json()
			return data['data']['subscribers']
		else:
			print("Invalid subreddit:", response.status_code)
			return 0
	
	except Exception as e:
		print('An error occurred:', e)
		return 0

#!/usr/bin/python3


import requests

def number_of_subscribers(subreddit):
	"""
	Function that queries the Reddit API and returns the number of subscribers.
	If the subreddit is invalid or any other error occurs, returns 0.
	"""

	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {'User-Agent': 'Custom User Agent'}

	try:
		response = requests.get(url, headers=headers, allow_redirects=False)
		
		if response.status_code == 200:
			data = response.json()
			return data['data']['subscribers']
		else:
			print("Invalid subreddit")
			return 0
	
	except Exception as e:
		print('An error occurred:', e)
		return 0

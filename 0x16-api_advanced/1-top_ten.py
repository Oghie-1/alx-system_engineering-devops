#!/usr/bin/python3
"""
API requests for top 10 reddit posts

"""

import requests

def top_ten(subreddit):
	"""
		Prints the top 10 posts from a subbreddit using the api callrequests.
	Returns: 0 on invalid requests
	"""
	url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
	headers = {'User-Agent': 'Custom User Agent/u/ResponsibleCup1157 for Holberton School'}
	response = requests.get(url, headers=headers)
	try:
		if response.status_code == 200:
			data = response.json().get('data')
			if data:
				children = data.get('children')
				if children:
					for post in children:
						print(post['data']['title'])
				else:
					print("No posts found in subreddit: {}".format(subreddit))
		else:
			print("Error: Unable to fetch data from Reddit. Status code: {}".format(response.status_code))
			return None
	except requests.exceptions.RequestException as e:
		print("Error: Unable to fetch data from reddit: {}".format(e))
		return 0
	except Exception as e:
		print ("An unexpected error occured: {e}".format(e))
		return 0

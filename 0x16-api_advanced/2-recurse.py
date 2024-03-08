#!/usr/bin/python3
"""
recursive function that queries the reddit API
returns a list containing articles for a 
given subreddit..
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
	"""
	 Recursive function that queries the Reddit API 
		and returns a list containing the titles 
		of all hot articlesfor a given subreddit.
		Returns None if no results are found for
		the given subreddit.
	"""
	url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
	headers = {'User-Agent': 'Custom User Agent/u/ResponsibleCup1157 for Holberton School'}
	
	# Parameters for the API request
	
	params = {'limit': 100}
	if after:
		params['after'] = after

	response = requests.get(url, headers=headers, params=params, allow_redirects=False)
	try:
		"""Raise an exception for HTTP errors (status_codes for 4xx and 5xx)"""
		response.raise_for_status()
		data = response.json().get('data')
		if data:
			children = data.get('children')
			if children:
				for post in children:
					hot_list.append(post['data']['title'])
				after = data.get('after')
				if after:
					return recurse(subreddit, hot_list, after)
				else:
					return hot_list
		return None #if no results are found

	except Exception as e:
		print("An error occured: {}".format(e))
		return None

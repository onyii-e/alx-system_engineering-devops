#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    # Base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom headers to avoid 429 Too Many Requests errors
    headers = {'User-Agent': 'MyRedditAPI/0.1'}
    
    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful and data is valid
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        # If the status code is not 200, the subreddit is likely invalid or other errors occurred
        return 0


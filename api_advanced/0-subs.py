#!/usr/bin/python3
import requests
def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
    return 0
data = response.json()
subscribers = data['data']['subscribers']
return subscribers

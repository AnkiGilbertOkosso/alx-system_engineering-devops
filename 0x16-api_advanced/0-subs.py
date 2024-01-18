#!/usr/bin/python3
"""Function to retrieve the number of subscribers for a
specific Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a specified subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /i/bdov_)"
    }
    response = requests.get(
        url,
        headers=request_headers,
        allow_redirects=False)
    if response.status_code != 200:
        return 0
    dic = response.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return response.json()['data']['subscribers']
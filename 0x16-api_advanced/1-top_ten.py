#!/usr/bin/python3
"""Function to retrieve and print the titles of the 10
hottest posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a specified subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    request_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /i/bdov_)"
    }
    request_params = {
        "limit": 10
    }
    response = requests.get(url, headers=request_headers, params=request_params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    api_data = response.json().get("data")
    [print(post.get("data").get("title")) for post in api_data.get("children")]
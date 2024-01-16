#!/usr/bin/python3
"""Function to retrieve the number of subscribers for a specific
Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a specified subreddit."""
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    api_response = requests.get(
            api_url,
            headers=request_headers,
            allow_redirects=False)

    if api_response.status_code == 404:
        return 0

    api_data = api_response.json().get("data")
    return api_data.get("subscribers")

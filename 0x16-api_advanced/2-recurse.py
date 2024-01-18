#!/usr/bin/python3
"""Function to retrieve a list of all hot posts
on a specified Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given
    subreddit using recursive calls."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    request_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /i/bdov_)"
    }
    request_params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=request_headers, params=request_params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    api_data = response.json().get("data")
    after = api_data.get("after")
    count += api_data.get("dist")
    for post in api_data.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
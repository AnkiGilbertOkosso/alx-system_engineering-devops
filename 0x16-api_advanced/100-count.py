#!/usr/bin/python3
"""Function to count occurrences of words in titles of
hot posts on a specified Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in titles of hot posts of a
    specified subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
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
    try:
        api_results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    api_results = api_results.get("data")
    after = api_results.get("after")
    count += api_results.get("dist")
    for post in api_results.get("children"):
        title_words = post.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title_words:
                times = len([t for t in title_words if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
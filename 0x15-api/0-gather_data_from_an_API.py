#!/usr/bin/python3
"""Retrieve and display TODO list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(api_url + "users/{}".format(sys.argv[1]))
    user_data = user_response.json()

    todos_response = requests.get(api_url + "todos",
                                  params={"userId": sys.argv[1]})
    todos_data = todos_response.json()

    completed_tasks = [
        task.get("title") for task in todos_data if task.get("completed")
        ]

    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(completed_tasks), len(todos_data)))

    [print("\t {}".format(task_title)) for task_title in completed_tasks]

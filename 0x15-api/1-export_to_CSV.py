#!/usr/bin/python3
"""Retrieve and export TODO list information
for a given employee ID in CSV format.
"""
import requests
import csv
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(api_url + "users/{}".format(sys.argv[1]))
    user_data = user_response.json()

    todos_response = requests.get(api_url + "todos",
                                  params={"userId": sys.argv[1]})
    todos_data = todos_response.json()

    csv_file_path = "{}.csv".format(sys.argv[1])

    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
            ])

        for task in todos_data:
            csv_writer.writerow([
                sys.argv[1],
                user_data.get("username"),
                str(task.get("completed")),
                task.get("title")
            ])

    print("Data exported to {}".format(csv_file_path))

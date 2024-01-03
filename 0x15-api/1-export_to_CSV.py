#!/usr/bin/python3
"""Export TODO list information for a
given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    api_url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(api_url + "users/{}".format(employee_id))
    user_data = user_response.json()

    username = user_data.get("username")

    todos_response = requests.get(api_url + "todos",
                                  params={"userId": employee_id})
    todos_data = todos_response.json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        [csv_writer.writerow(
            [employee_id, username, task.get("completed"), task.get("title")]
         ) for task in todos_data]

        print("Data exported to {}.csv".format(employee_id))

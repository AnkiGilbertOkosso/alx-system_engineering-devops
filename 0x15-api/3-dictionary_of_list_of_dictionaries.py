#!/usr/bin/python3
"""Exports each employee's to-do list information to JSON format."""
import json
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    employees_data = requests.get(api_url + "users").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            employee.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee.get("username")
            } for task in requests.get(api_url + "todos",
                                       params={
                                           "userId": employee.get("id")
                                           }).json()]
            for employee in employees_data}, json_file)

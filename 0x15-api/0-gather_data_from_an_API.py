#!/usr/bin/python3
"""
Python script that, using the JSON PLACEHOLDER API,
for a given employee ID, returns information about his/her TODO list progress
"""

import requests
import sys


def get_data_from_api(uid):
    """
    Gets and prints data from JSON PLACEHOLDER API

    Args:
        uid (str): employee id

    Returns:
        None
    """
    base = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{base}users/{uid}").json()
    user_todos = requests.get(f"{base}todos", params={"userId": uid}).json()
    completed = [todo.get("title") for todo in user_todos if todo.get("completed")]
    output = "Employee {:<18} is done with tasks({:<16}):".format(
        user.get("name"), "{}/{}".format(len(completed), len(user_todos))
    )
    print("\n{:<26}".format(output))
    print("\n".join(completed))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = str(sys.argv[1])
        get_data_from_api(employee_id)
    except ValueError:
        print("Error: Employee ID must be a valid integer")

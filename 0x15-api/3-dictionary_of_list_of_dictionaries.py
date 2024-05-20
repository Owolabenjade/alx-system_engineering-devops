#!/usr/bin/python3
"""
This module fetches and exports the TODO list data for all employees from a
REST API to a JSON file.

Usage:
    python3 3-dictionary_of_list_of_dictionaries.py

The JSON file format is:
{
    "USER_ID": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
        },
        ...
    ],
    ...
}

The output JSON file will be named 'todo_all_employees.json'.
"""

import json
import requests


def fetch_all_employees():
    """
    Fetches data for all employees from the API.

    Returns:
        list: A list of dictionaries containing employee data if the request is
        successful.
        None: If the request is unsuccessful.
    """
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def fetch_todos():
    """
    Fetches TODO list data for all employees from the API.

    Returns:
        list: A list of dictionaries containing TODO list data if the request
        is successful.
        None: If the request is unsuccessful.
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def export_to_json(data):
    """
    Exports the TODO list data to a JSON file.

    Args:
        data (dict): A dictionary containing the TODO list data for all employees.
    """
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    """
    Main entry point of the script. Fetches and exports the TODO list data for
    all employees to a JSON file.
    """
    # Fetch all employee data
    employees = fetch_all_employees()
    if not employees:
        print("Could not fetch employee data.")
        sys.exit(1)

    # Fetch all TODO list data
    todos = fetch_todos()
    if not todos:
        print("Could not fetch TODO list data.")
        sys.exit(1)

    # Organize data
    all_data = {}
    for employee in employees:
        employee_id = employee.get('id')
        username = employee.get('username')
        user_todos = [
            {
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            }
            for todo in todos if todo.get('userId') == employee_id
        ]
        all_data[str(employee_id)] = user_todos

    # Export to JSON
    export_to_json(all_data)

#!/usr/bin/python3
"""
This module fetches and displays the TODO list progress of a given employee
from a REST API and exports the data to a JSON file.

Usage:
    python3 2-export_to_JSON.py <employee_id>

Arguments:
    <employee_id> - The ID of the employee whose TODO list progress is to be
    fetched and exported to a JSON file.

Example:
    python3 2-export_to_JSON.py 2
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches employee data from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: A dictionary containing employee data if the request is
        successful.
        None: If the request is unsuccessful.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def fetch_todos(employee_id):
    """
    Fetches TODO list data for the given employee ID from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: A list of dictionaries containing TODO list data if the request
        is successful.
        None: If the request is unsuccessful.
    """
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def export_to_json(employee_id, username, todos):
    """
    Exports TODO list data to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        username (str): The username of the employee.
        todos (list): A list of dictionaries containing TODO list data.
    """
    tasks = []
    for todo in todos:
        task = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        tasks.append(task)
    data = {str(employee_id): tasks}
    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    """
    Main entry point of the script. Fetches and prints the TODO list progress
    of an employee based on the provided employee ID, and exports the data to a
    JSON file.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch employee data
    employee = fetch_employee_data(employee_id)
    if not employee:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    employee_name = employee.get('name')
    username = employee.get('username')

    # Fetch TODO list data
    todos = fetch_todos(employee_id)
    if not todos:
        print(f"Could not fetch TODO list for employee with ID {employee_id}.")
        sys.exit(1)

    # Calculate TODO progress
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the results
    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    # Export to JSON
    export_to_json(employee_id, username, todos)

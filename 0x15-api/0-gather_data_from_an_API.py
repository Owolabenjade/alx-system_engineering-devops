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
        uid: employee id
    Return:
        None
    """
    base = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user data
    user_response = requests.get(base + "users/" + str(uid))
    if user_response.status_code != 200:
        print("Failed to retrieve user data")
        return
    user = user_response.json()
    
    # Fetch todos data
    todos_response = requests.get(base + "todos", params={"userId": uid})
    if todos_response.status_code != 200:
        print("Failed to retrieve todos data")
        return
    userTodos = todos_response.json()
    
    completed = [todo.get("title") for todo in userTodos if todo.get("completed")]
    output = "Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(userTodos))
    
    # Ensure proper formatting
    task_output = "\n\t ".join([output] + completed)
    print(task_output)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
    else:
        try:
            employee_id = int(sys.argv[1])
            get_data_from_api(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")

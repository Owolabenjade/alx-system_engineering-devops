#!/usr/bin/python3
"""
Script that retrieves TODO list progress for a given employee ID using REST API
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays TODO list progress for a specific employee
    Args:
        employee_id: Integer ID of the employee
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("Error: Employee not found")
        return
    
    employee = user_response.json()
    employee_name = employee.get('name')
    
    # Get TODO list for employee
    todos_response = requests.get(f"{base_url}/todos", 
                                params={'userId': employee_id})
    if todos_response.status_code != 200:
        print("Error: Could not retrieve TODO list")
        return
    
    todos = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo.get('completed')])
    
    # Display progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    
    # Display completed tasks
    for todo in todos:
        if todo.get('completed'):
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

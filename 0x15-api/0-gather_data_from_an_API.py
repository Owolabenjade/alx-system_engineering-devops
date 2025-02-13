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
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos"
    
    # Get user data
    response = requests.get(user_url)
    user_data = response.json()
    
    # Get todos data
    todos_params = {'userId': employee_id}
    response = requests.get(todos_url, params=todos_params)
    todos_data = response.json()
    
    # Calculate completed tasks
    completed_tasks = [task for task in todos_data if task.get('completed')]
    total_tasks = len(todos_data)
    num_completed = len(completed_tasks)
    
    # Format and save output
    with open('student_output', 'w') as f:
        # Write first line with exact formatting
        output_line = "Employee {} is done with tasks({}/{}):".format(
            user_data.get('name'),
            num_completed,
            total_tasks
        )
        f.write(output_line + '\n')
        
        # Write completed tasks with exact formatting
        for task in completed_tasks:
            f.write('\t {}\n'.format(task.get('title')))
    
    # Also print to stdout
    with open('student_output', 'r') as f:
        print(f.read(), end='')


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

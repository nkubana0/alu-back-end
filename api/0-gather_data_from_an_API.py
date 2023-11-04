#!/usr/bin/python3

"""Retrieve and display an employee's TODO list progress"""

import sys
import urllib.request
import json


def get_employee_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Retrieve user information
    user_url = f"{base_url}/users/{employee_id}"
    user_response = urllib.request.urlopen(user_url)
    user_data = json.loads(user_response.read().decode())

    if "name" not in user_data:
        print(f"Failed to retrieve user data for employee ID {employee_id}")
        return

    employee_name = user_data["name"]

    # Retrieve TODO list information
    todo_url = f"{base_url}/todos?userId={employee_id}"
    todo_response = urllib.request.urlopen(todo_url)
    todo_data = json.loads(todo_response.read().decode())

    completed_tasks = [task for task in todo_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todo_data)

    # Print TODO list progress
    print(
        f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):"
    )
    for task in completed_tasks:
        print(f'    {task["title"]}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_list_progress(employee_id)
        except ValueError:
            print("Invalid employee ID. Please provide an integer.")

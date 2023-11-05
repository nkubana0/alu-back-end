#!/usr/bin/python3

"""Module for fetching and displaying employee TODO list progress."""

import requests
import sys

def get_employee_todo_list_progress(employee_id):
    """
    Fetches and displays an employee's TODO list progress.

    Args:
        employee_id (str): The ID of the employee to retrieve TODO list progress for.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        if (
            user_response.status_code != 200 or
            todo_response.status_code != 200
        ):
            print(f"Failed to retrieve data for employee ID {employee_id}")
            return

        user_data = user_response.json()
        employee_name = user_data["name"]

        tasks_data = todo_response.json()
        completed_tasks = [task for task in tasks_data if task["completed"]]
        num_completed_tasks = len(completed_tasks)
        total_num_tasks = len(tasks_data)

        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")

        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print("An error occurred while making the API request:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_list_progress(employee_id)

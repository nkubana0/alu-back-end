#!/usr/bin/python3

"""Module"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code == 200:
        user_data = user_response.json()
        employee_name = user_data['name']

        if todo_response.status_code == 200:
            todo_data = todo_response.json()
            completed_tasks = [task for task in todo_data if task['completed']]
            num_completed = len(completed_tasks)
            total_tasks = len(todo_data)

            print(f'Employee {employee_name} is done with tasks '
                  f'({num_completed}/{total_tasks}):')

            for task in completed_tasks:
                print(f'\t {task["title"]}')
        else:
            print(
                f'Failed to retrieve tasks data for employee ID {employee_id}')
    else:
        print(f'Failed to retrieve user data for employee ID {employee_id}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Usage: python3 script_name.py <employee_id>')
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

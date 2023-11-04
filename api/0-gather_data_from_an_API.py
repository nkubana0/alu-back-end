#!/usr/bin/python3

"""Module"""

import requests
import sys

"""Function that GETS the data from the API"""


def get_employee_todo_list_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    response = requests.get(user_url)

    if response.status_code == 200:
        user_data = response.json()
        employee_name = user_data['name']

        tasks_url = f'{base_url}/todos?userId={employee_id}'
        tasks_response = requests.get(tasks_url)

        if tasks_response.status_code == 200:
            tasks_data = tasks_response.json()
            completed_tasks = [
                task for task in tasks_data if task['completed']
            ]
            num_completed_tasks = len(completed_tasks)
            total_num_tasks = len(tasks_data)

            print(f'Employee {employee_name} is done with tasks '
                  f'({num_completed_tasks}/{total_num_tasks}):')

            for task in completed_tasks:
                print(f'\t {task["title"]}')
        else:
            print(
                f'Failed to retrieve tasks data for employee ID {employee_id}')
    else:
        print(f'Failed to retrieve user data for employee ID {employee_id}')


if __name__ == "__main__"
   if len(sys.argv) != 2:
        print(f"Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_list_progress(employee_id)

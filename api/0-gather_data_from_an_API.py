#!/usr/bin/python3
""" Library to gather data from an API """

import requests
import sys

""" Function to gather data from an API """

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todo = todo.format(employee_id)

    user_info = requests.request("GET", url).json()
    todo_info = requests.request("GET", todo).json()

    employee_name = user_info.get("name")
    total_tasks = list(filter(lambda x: (x["completed"] is True), todo_info))
    task_com = len(total_tasks)
    total_task_done = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          task_com, total_task_done))

    [print("\t {}".format(task.get("title"))) for task in total_tasks]



    #!/usr/bin/python3

"""Employee TODO progress"""

import requests
import sys


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


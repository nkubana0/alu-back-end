#!/usr/bin/python3
"""
a Python script that, using REST API,
returns information about employee TODO list progress.
"""
if __name__ == "__main__":
    import json
    import sys
    import urllib.request

    """
    format the employees id with the url
    """
    employee_id = sys.argv[1]
    url1 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url2 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/"
    req_object1 = urllib.request.Request(url1, method="GET")
    req_object2 = urllib.request.Request(url2, method="GET")
    with urllib.request.urlopen(req_object1) as response_object1:
        response1 = json.load(response_object1)
    with urllib.request.urlopen(req_object2) as response_object2:
        response2 = json.load(response_object2)
    completed_tasks = []
    for task in response1:
        if task['completed'] is not True:
            continue
        completed_tasks.append(task)
    no_of_comptasks = len(completed_tasks)
    totalno_of_task = len(response1)
    employee_name = response2["name"]
    print(f"Employee {employee_name} is done with tasks({no_of_comptasks}/\
{totalno_of_task}):")
    for comp_tasks in completed_tasks:
        print(f"\t {comp_tasks['title']}")

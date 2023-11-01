import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct the URL for the employee's TODO list
    todo_url = f"{base_url}/todos?userId={employee_id}"
    user_url = f"{base_url}/users/{employee_id}"

    try:
        # Fetch TODO list and user information from the API
        todo_response = requests.get(todo_url)
        user_response = requests.get(user_url)

        # Check if the API requests were successful
        if todo_response.status_code != 200 or user_response.status_code != 200:
            print("Employee not found or API request failed.")
            return

        todos = todo_response.json()
        user = user_response.json()

        # Calculate the number of completed and total tasks
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo['completed'])

        # Display employee TODO list progress
        print(f"Employee {user['name']} is done with tasks({completed_tasks}/{total_tasks}):")
        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print("An error occurred while making the API request:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)


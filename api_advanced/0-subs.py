#!/usr/bin/python3
import requests
def get_emp_todo(emp_id):
    URL = f"https//jsonplaceholder.typicode.com/users/{emp_id}/todos"
    emp_todo = requests.get(URL).json{}
    total_todos=len(emp_todo)
    completed_todos = 0
    for todo in emp todo:
        if todo("completed"):
            completed_todos += 1
    print(f"Out of {total_todos} total, completed todos are: {completed_todos})

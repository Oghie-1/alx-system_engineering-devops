#!/usr/bin/python3
"""Script that uses REST API"""
import json
import requests


def make_all(users=None, todos=None):
    """Turns all payloads into JSON format"""
    all_json = {}
    with open("todo_all_employees.json", "w") as f:
        for user in users:
            user_id = user.get("id")
            user_list = []
            for todo in todos:
                if user_id == todo.get("userId"):
                    user_list.append({
                        "username": user.get("username"),
                        "task": todo.get("title"),
                        "completed": todo.get("completed")
                    })
            all_json[user_id] = user_list
        json.dump(all_json, f)


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    make_all(users, todos)

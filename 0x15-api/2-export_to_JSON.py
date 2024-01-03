#!/usr/bin/python3
"""Script that uses REST API"""
import json
import requests
import sys


def make_json(users=None, todos=None, user_id=None):
    """Turns payloads into JSON format"""
    all_list = []
    with open(sys.argv[1] + ".json", "w") as f:
        for i in todos:
            all_list.append({
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": users[0].get("username")
            })
        all_json = {str(user_id): all_list}
        json.dump(all_json, f)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args_id = {"id": sys.argv[1]}
        users = requests.get("https://jsonplaceholder.typicode.com/users",
                             params=args_id).json()
        args_user_id = {"userId": sys.argv[1]}
        todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                             params=args_user_id).json()

        make_json(users, todos, sys.argv[1])

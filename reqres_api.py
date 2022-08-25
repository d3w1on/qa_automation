import requests
import users
import json

url = "https://reqres.in/api"

# headers should be moved out of this file
# headers = {
#     "User-Agent": "test"
# }


def register_successful(payload):
    return requests.post(f"{url}/register", data=payload)


def get_users_list(page):
    return requests.get(f"{url}/users?page={page}")


def get_single_user(userId):
    return requests.get(f"{url}/users/{userId}")



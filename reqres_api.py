import requests
import users
import json

url = "https://reqres.in/api"


# headers should be moved out of this file
# headers = {
#     "User-Agent": "test"
# }

#######################################
def register_successful(payload):
    return requests.post(f"{url}/register", data=payload)


# Payload Sample below

# payload = {
#   "email": "eve.holt@reqres.in",
#   "password": "pistol"
# }
#######################################
def get_users_list(params):
    return requests.get(f"{url}/users", params=params)


# Params Sample below

# params = {"page": 1}
#######################################
def get_single_user(userId):
    return requests.get(f"{url}/users/{userId}")


# userId as int value in range 1 - 12
#######################################

def login(payload):
    users.user.update(json.loads(requests.post(f"{url}/login", data=payload).text))
    return requests.post(f"{url}/login", data=payload)


# Payload Sample below
#
# payload = {
#   "email": "eve.holt@reqres.in",
#   "password": "pistol"
# }
########################################
def create_user(body):
    return requests.post(f"{url}/users", data=body)

# Body Sample below
#
# body = {
#     "name": "morpheus",
#     " job": "leader"
# }
###########################################


print(create_user(body = {
    "key": "morpheus",
    "value": "leader"
}).text)

#######################################

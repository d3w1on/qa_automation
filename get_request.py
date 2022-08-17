import requests
import json

headers = {
    "User-Agent": "test"
}

url = "https://gorest.co.in"

resp = requests.get(f"{url}/public/v2/users", headers=headers)


def prettify(s):
    return s.strip("[]").replace("},", "}  ").split("  ")

ldata = prettify(resp.content.decode())

print(f"Status code: {resp.status_code}\nHeaders: \n{(json.dumps(dict(resp.headers), indent=4))} \nBody: \n")

for i in ldata:
    print(i)




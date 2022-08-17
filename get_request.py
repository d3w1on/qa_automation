import requests
import json

headers = {
    "User-Agent": "test"
}

url = "https://gorest.co.in"

resp = requests.get(f"{url}/public/v2/users", headers=headers)

print(f"Status code: {resp.status_code}\nHeaders: \n{(json.dumps(dict(resp.headers), indent=4))}")

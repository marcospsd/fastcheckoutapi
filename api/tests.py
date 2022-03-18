import requests
import json
from requests.auth import HTTPBasicAuth

url = 'http://127.0.0.1:8000/auth/'
body = {
    "username": "",
    "password": ""
}
data = requests.post(url, data=body)
print(data.json())

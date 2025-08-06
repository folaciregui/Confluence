import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://frba-utn-edu.atlassian.net/wiki/rest/api/content/"

auth = HTTPBasicAuth("folacireguibonilla@frba.utn.edu.ar", "x") # poner tu token

headers = {
    "Content-Type": "application/json"
}

data = {
    "type": "page",
    "title": "Prueba 3",
    "space": {"key": "FRBAUTNEDU"},
    "body": {
        "storage": {
            "value": "<p>Prueba 3.</p>",
            "representation": "storage"
        }
    }
}

response = requests.post(url, headers=headers, auth=auth, data=json.dumps(data))

print(response.status_code)
print(response.json())

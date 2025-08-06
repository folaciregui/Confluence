import requests
from requests.auth import HTTPBasicAuth
import json

domain = "frba-utn-edu.atlassian.net"
email = "folacireguibonilla@frba.utn.edu.ar"
api_token = "x" # poner tu token
space_key = "FRBAUTNEDU"

# Busca las páginas del espacio
url = f"https://{domain}/wiki/rest/api/content?spaceKey={space_key}&type=page&expand=body.storage&limit=50"

response = requests.get(
    url,
    auth=HTTPBasicAuth(email, api_token),
    headers={"Accept": "application/json"}
)

if response.status_code == 200:
    data = response.json()
    pages = data.get("results", [])
    
    for page in pages:
        title = page.get("title")
        html_body = page.get("body", {}).get("storage", {}).get("value", "")
        
        print("="*60)
        print(f"Título: {title}")
        print("-"*60)
        print(html_body)
        print("="*60 + "\n\n")
else:
    print(f"Error {response.status_code}: {response.text}")

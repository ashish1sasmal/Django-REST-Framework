import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

def update(id):
    json_data = json.dumps({"id":id,"name":"Bellatrix"})
    print(json_data)
    print(BASE_URL+ENDPOINT)
    resp = requests.put(BASE_URL+ENDPOINT,data=json_data)
    print(resp.status_code)
    # print(resp.text)
    print(resp.json())


def get():
    resp = requests.get(BASE_URL+ENDPOINT)
    print(resp.json())

update(10)

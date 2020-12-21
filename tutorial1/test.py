import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api2/"

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
    print(resp.status_code)
    print(resp.json())

def delete():
    resp = requests.delete(BASE_URL+ENDPOINT+str(5))
    print(resp.status_code)
    print(resp.json())

def update():
    resp = requests.put(BASE_URL+ENDPOINT+str(5), data=json.dumps({"name":"Tonks"}))
    print(resp.status_code)
    print(resp.json())

get()

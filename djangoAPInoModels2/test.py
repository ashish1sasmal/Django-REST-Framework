import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
END_POINT = "api/"

def crud_get(id=None):
    data={}
    if id is not None:
        data = {
            "id":id
        }
    resp = requests.get(BASE_URL+END_POINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

def crud_post(id=None):
    data ={
        "name": "Snape",
        "rollno": 0,
        "marks": 85,
        "gf": "Lily",
        "bf": "James"
    }
    json_data = json.dumps(data)

    resp = requests.post(BASE_URL+END_POINT, data=json_data)
    print(resp.status_code)
    print(resp.json())

def crud_put(id=None):
    data ={
        "id":id,
        "gf": "Lily",
        "bf": "Sirius"
    }
    json_data = json.dumps(data)

    resp = requests.put(BASE_URL+END_POINT, data=json_data)
    print(resp.status_code)
    print(resp.json())

def crud_delete(id=None):
    data ={}
    if id is not None:
        data = {
        "id":id
        }
    json_data = json.dumps(data)

    resp = requests.delete(BASE_URL+END_POINT, data=json_data)
    print(resp.status_code)
    print(resp.json())

crud_put(4)

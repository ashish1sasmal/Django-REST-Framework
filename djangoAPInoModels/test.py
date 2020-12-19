import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
END_POINT = "api/"

def get_resource(*args):
    resp = requests.get(BASE_URL+END_POINT+str(args[0]))
    print("Status Code : ",resp.status_code)

    # if resp.status_code in range(200,300):
    if resp.status_code == requests.codes.ok:
        print(resp.json())
    else:
        print("Some thing wrong")

def get_all(*args):
    resp = requests.get(BASE_URL+END_POINT)
    print("Status Code : ",resp.status_code)
    print(resp.json())

def get_resource2(*args):
    resp = requests.get(BASE_URL+END_POINT+str(args[0]))
    print("Status Code : ",resp.status_code)
    print(resp.json())

def createEmp():
    new_emp = {
        "enum":31,
        "ename":"Dobby",
        "esal":8000,
        "eaddr":"Hogsmeade"
    }

    json_data = json.dumps(new_emp)

    resp = requests.post(BASE_URL+END_POINT, data=json_data)
    print(resp.status_code)
    print(resp.json())

def update(id):
    new_emp = {
        "esal":8990,
        "eaddr":"Burrow"
    }
    resp = requests.put(BASE_URL+END_POINT+str(id),data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


def delete(id):
    resp = requests.delete(BASE_URL+END_POINT+str(id))
    print(resp.status_code)
    print(resp.json())

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
        "enum":45,
        "ename":"Remus Lupin",
        "esal":500,
        "eaddr":"Shreiking Shack"
    }
    json_data = json.dumps(data)

    resp = requests.post(BASE_URL+END_POINT, data=json_data)
    print(resp.status_code)
    print(resp.json())

def crud_put(id=None):
    data ={
        "id":id,
        "esal":450,
        "eaddr":"Shreiking Shack"
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
crud_put(9)

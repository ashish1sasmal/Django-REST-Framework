import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
END_POINT = "details/"

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

createEmp()
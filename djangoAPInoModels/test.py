import requests

BASE_URL = "http://127.0.0.1:8000/"
END_POINT = "details/"

def resource(*args):
    resp = requests.get(BASE_URL+END_POINT+str(args[0]))
    print(resp.status_code)
    print(resp.json())

resource(3)
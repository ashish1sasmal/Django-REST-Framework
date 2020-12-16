
import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apijson'

response = requests.get(BASE_URL+END_POINT)

#c onverts json to dict
print(response.json())
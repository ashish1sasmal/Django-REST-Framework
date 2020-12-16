from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emp_data_view(request):
    emp_data={
        "eno":100,
        "ename":"Ashish",
        'eaddr':"Delhi",
        'esal':'120000'
    }
    resp = f"<h2>Employee no : {emp_data['eno']} <br>Employee name : <i>{emp_data['ename']}</i> <br>Employee Salary : {emp_data['esal']} <br>Employee Address : {emp_data['eaddr']}</h2>"

    return HttpResponse(resp)

import json
def emp_data_json_view(request):
    emp_data={
        "eno":100,
        "ename":"Ashish",
        'eaddr':"Delhi",
        'esal':'120000'
    }
    json_data = json.dumps(emp_data)
    print(json_data)

    #MIME Type (Muti-purpose Internet Mail Extension)
    return HttpResponse(json_data, content_type='application/json') 

from django.http import JsonResponse

def emp_data_json_view2(request):
    emp_data={
        "eno":100,
        "ename":"Ashish",
        'eaddr':"Delhi",
        'esal':'120000'
    }
    # json dumps() not needed coz it's included
    #MIME Type (Muti-purpose Internet Mail Extension)
    return JsonResponse(emp_data) 

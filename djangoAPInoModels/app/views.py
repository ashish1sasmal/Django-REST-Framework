from django.shortcuts import render

# Create your views here.

from .models import *
from django.views.generic import View
from django.http import HttpResponse
import json

class EmployeeDetailsCBV(View):
    def get(self,request,*args,**kwargs):
        try:
            data = Employee.objects.get(id=kwargs["id"])
            resp = {
                "Enum":data.enum,
                "Ename":data.ename,
                "Esal":data.esal,
                "Eaddr":data.eaddr
                }
            resp = json.dumps(resp)
            print(resp)
            return HttpResponse(resp,content_type="application/json")
        except:
            return HttpResponse("<h1>Some Error Occured!</h1>")
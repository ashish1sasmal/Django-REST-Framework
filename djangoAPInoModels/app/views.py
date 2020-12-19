from django.shortcuts import render

# Create your views here.

from .models import *
from django.views.generic import View
from django.http import HttpResponse
import json
from django.core.serializers import serialize

class EmployeeDetailsCBV(View):
    def get(self,request,*args,**kwargs):
        try:
            data = Employee.objects.filter(id=kwargs["id"])
            
            # select particular fields only to serialize using fields argument
            # exclude will not in work here
            json_data = serialize('json',data,fields=('enum','ename','eaddr'))
            print(json_data)
            return HttpResponse(json_data,content_type="application/json")
        except:
            return HttpResponse("<h1>Some Error Occured!</h1>")
from django.shortcuts import render

# Create your views here.

from .models import *
from django.views.generic import View
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from .mixins import SerializeMixin,HttpResponseMixin


class EmployeeDetailsCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        try:
            data = Employee.objects.get(id=kwargs["id"])

        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'Requested resource not available'})
            status_code = 404

        else:   # else will excecute only when no error is occured.

            # select particular fields only to serialize using fields argument
            # exclude will not in work here
            print(data)
            json_data = serialize('json',[data,],fields=('enum','ename','eaddr'))
            print(json_data)
            status_code=200
        return self.render_to_http(json_data,status_code)


class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        try:
            qs = Employee.objects.all()
            json_data = self.serialize(qs)
            status_code=200
        except :
            json_data = json.dumps({'msg':'Requested resource not available'})
            status_code = 404

        return self.render_to_http(json_data,status_code)

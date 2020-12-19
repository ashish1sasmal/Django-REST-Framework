from django.shortcuts import render

# Create your views here.

from .models import *
from django.views.generic import View
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from .mixins import SerializeMixin,HttpResponseMixin

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .utils import is_json

from .forms import EmployeeForm


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


@method_decorator(csrf_exempt, name='dispatch')
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
    
    def post(self,request,*args,**kwargs):
        data = request.body
        print(data)
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please Send valid json data"})
            return self.render_to_http(json_data,400)
        else:
            emp_data = json.loads(data)
            form = EmployeeForm(emp_data)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({"msg":"Resource created successfully!"})
                return self.render_to_http(json_data,200)
            if form.errors :
                json_data = json.dumps(form.errors)
                return self.render_to_http(json_data,400)
            

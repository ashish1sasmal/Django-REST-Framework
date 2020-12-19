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

from .utils import *

from .forms import EmployeeForm

@method_decorator(csrf_exempt, name='dispatch')
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

    def put(self,request,*args,**kwargs):
        emp = get_object_by_id(kwargs["id"])
        if emp is None:
            json_data = json.dumps({'msg':'Updation failed. No match found.'})
            status_code = 404
            return self.render_to_http(json_data,status_code)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please Send valid json data"})
            return self.render_to_http(json_data,400)

        emp_data_json = self.serialize([emp,])
        emp_data_dict = json.loads(emp_data_json)[0]
        print(emp_data_dict)
        provided_data = json.loads(data)
        emp_data_dict.update(provided_data)

        form = EmployeeForm(emp_data_dict,instance=emp)
        # without instance new record will be created
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg":"Resource updated successfully!"})
            return self.render_to_http(json_data,200)
        if form.errors :
            json_data = json.dumps(form.errors)
            return self.render_to_http(json_data,400)

    def delete(self,request,*args,**kwargs):
        emp = get_object_by_id(kwargs["id"])
        if emp is None:
            json_data = json.dumps({'msg':'Deletion failed. No match found.'})
            status_code = 404
            return self.render_to_http(json_data,status_code)
        # returns tuple 1. status 2. Deleted item
        status,item = emp.delete()
        if status==1:
            json_data = json.dumps({"msg":"Resource deleted successfully!"})
            return self.render_to_http(json_data,200)
        else:
            json_data = json.dumps({"msg":"Unable to delete. Please try again."})
            return self.render_to_http(json_data,500)

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

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json =  is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please Send valid json data"})
            return self.render_to_http(json_data,400)

        dict_data = json.loads(data)
        id = dict_data.get('id',None)
        if id is not None:
            emp = get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({"msg":"No match Found"})
                status_code = 404
                return self.render_to_http(json_data,status_code)

            json_data = self.serialize([emp])
            return self.render_to_http(json_data)

        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http(json_data)

    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json =  is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please Send valid json data"})
            return self.render_to_http(json_data,400)

        dict_data = json.loads(data)
        form = EmployeeForm(dict_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg":"Resource Created successfully."})
            return self.render_to_http(json_data)
        else:
            json_data = json.dumps(form.errors)
            return self.render_to_http(json_data,400)

    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json =  is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please Send valid json data"})
            return self.render_to_http(json_data,400)

        dict_data = json.loads(data)
        id = dict_data.get('id',None)
        if id is not None:
            emp = get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({"msg":"No match Found"})
                status_code = 404
                return self.render_to_http(json_data,status_code)

            emp_json_data = self.serialize([emp])
            emp_dict_data = json.loads(emp_json_data)[0]
            print(emp_dict_data)
            emp_dict_data.update(dict_data)
            form = EmployeeForm(emp_dict_data,instance=emp)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({"msg":"Resource Updated successfully."})
                return self.render_to_http(json_data)
            else:
                json_data = json.dumps(form.errors)
                return self.render_to_http(json_data,400)
        else:
            json_data = json.dumps({"msg":"Please provide id."})
            return self.render_to_http(json_data,400)

    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json =  is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please Send valid json data"})
            return self.render_to_http(json_data,400)

        dict_data = json.loads(data)
        id = dict_data.get('id',None)
        if id is not None:
            emp = get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({"msg":"No match Found"})
                status_code = 404
                return self.render_to_http(json_data,status_code)

            status,empdata = emp.delete()
            if status==1:
                json_data = json.dumps({"msg":"Resource Deleted successfully."})
                return self.render_to_http(json_data)
            else:
                json_data = json.dumps({"msg":"Some error occured. Please try again."})
                status_code = 500
                return self.render_to_http(json_data,status_code)
        else:
            json_data = json.dumps({"msg":"Please provide id."})
            return self.render_to_http(json_data,400)

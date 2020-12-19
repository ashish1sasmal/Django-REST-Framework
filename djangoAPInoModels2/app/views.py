from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse
from .mixins import SerializeMixin,HttpResponseMixin

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json
from .utils import *

from .forms import StudentForm

@method_decorator(csrf_exempt, name='dispatch')
class StudentCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json =  is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please Send valid json data"})
            return self.render_to_http(json_data,400)

        dict_data = json.loads(data)
        id = dict_data.get('id',None)
        if id is not None:
            std = get_object_by_id(id)
            if std is None:
                json_data = json.dumps({"msg":"No match Found"})
                status_code = 404
                return self.render_to_http(json_data,status_code)

            json_data = self.serialize([std])
            return self.render_to_http(json_data)

        qs = Student.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http(json_data)

    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json =  is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"Please Send valid json data"})
            return self.render_to_http(json_data,400)

        dict_data = json.loads(data)
        form = StudentForm(dict_data)
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
            std = get_object_by_id(id)
            if std is None:
                json_data = json.dumps({"msg":"No match Found"})
                status_code = 404
                return self.render_to_http(json_data,status_code)

            std_json_data = self.serialize([std])
            std_dict_data = json.loads(std_json_data)[0]
            print(std_dict_data)
            std_dict_data.update(dict_data)
            form = StudentForm(std_dict_data,instance=std)
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
            std = get_object_by_id(id)
            if std is None:
                json_data = json.dumps({"msg":"No match Found"})
                status_code = 404
                return self.render_to_http(json_data,status_code)

            status,stddata = std.delete()
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

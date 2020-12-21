from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
import json
from .models import Student
from .serializers import StudentSerializer2, UserSerializer
from .mixins import HttpResponseMixin, SerializeMixin

from .utils import is_json, get_object_by_id

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentMixCBV(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer2
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly
                        ]

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StudentList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer2
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly
                        ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentDetailCBV(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer2
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly
                        ]

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self,request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

@method_decorator(csrf_exempt,name='dispatch')
class StudentCBV(APIView):
    def get(self,request,format=None,*args,**kwargs):
        students = Student.objects.all()
        seri = StudentSerializer2(students,many=True)
        return Response(seri.data,status=status.HTTP_200_OK)

    def post(self,request,format=None,*args,**kwargs):
        # try:
            dict_data = request.data
            print(dict_data,type(dict_data))
            seri = StudentSerializer2(data=dict_data)
            if seri.is_valid():
                seri.save()
                json_msg = json.dumps({"msg":"Resource created successfully"})
                return Response(json_msg,status.HTTP_201_CREATED)
            else:
                json_msg = json.dumps(seri.errors)
                return Response(json_msg,status.HTTP_400_BAD_REQUEST)
        # except:
        #     json_msg = json.dumps({"msg":"Some error occured!"})
        #     return self.render_to_http(json_msg,500)

    def put(self,request,format=None,*args,**kwargs):
        # try:
            dict_data = request.data
            print(dict_data)
            id = dict_data.get("id",None)
            if id is None:
                json_msg = json.dumps({"msg":"Please give id value."})
                return Response(json_msg,status.HTTP_400_BAD_REQUEST)

            std = get_object_by_id(id)
            if std is None:
                json_msg = json.dumps({"msg":"Match not found."})
                return Response(json_msg,status.HTTP_404_NOT_FOUND)
            print(std)
            seri = StudentSerializer2(std,data=dict_data,partial=True)
            if seri.is_valid():
                seri.save()
                json_msg = json.dumps({"msg":"Resource updated successfully"})
                return Response(json_msg,status.HTTP_206_PARTIAL_CONTENT)
            else:
                json_msg = json.dumps(seri.errors)
                return Response(json_msg,status.HTTP_400_BAD_REQUEST)
        # except:
        #     json_msg = json.dumps({"msg":"Some error occured!"})
        #     return self.render_to_http(json_msg,500)

    def delete(self,request,format=None,*args,**kwargs):
        # try:
            dict_data = request.data
            print(dict_data)
            id = dict_data.get("id",None)
            if id is None:
                json_msg = json.dumps({"msg":"Please give id value."})
                return Response(json_msg,status.HTTP_400_BAD_REQUEST)

            std = get_object_by_id(id)
            if std is None:
                json_msg = json.dumps({"msg":"Match not found."})
                return Response(json_msg,status.HTTP_404_NOT_FOUND)
            status_code,item = std.delete()
            if status_code==1:
                json_msg = json.dumps({"msg":"Resource deleted successfully"})
                return Response(json_msg,status.HTTP_200_OK)
            else:
                json_msg = json.dumps(seri.errors)
                return Response(json_msg,status.HTTP_500_INTERNAL_SERVER_ERROR)
        # except:
        #     json_msg = json.dumps({"msg":"Some error occured!"})
        #     return self.render_to_http(json_msg,500)

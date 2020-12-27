from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import *
from rest_framework import mixins, status
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)
        token, created = Token.objects.get_or_create(user=user)
        print(token,created)
        return Response({
                'token':token.key,
                'user_id':user.username
        })


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class AlbumCbv(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly
                        ]

    def get(self,request,format=None,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class TrackCbv(generics.GenericAPIView,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,mixins.UpdateModelMixin):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly
                        ]

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,id=kwargs["pk"],*args,**kwargs)

@api_view(['GET'])
def trackdetail(request,pk):
    tracks = Track.objects.get(id=pk)
    seri = TrackSerializer(tracks)
    return Response(seri.data,status=status.HTTP_200_OK)

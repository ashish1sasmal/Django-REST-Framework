from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
import json

class TrackSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(many=False, read_only=False,queryset=Album.objects.all())
    class Meta:
        model = Track
        fields = ['title','duration','genre','album']
        # fields = "__all__"

    def create(self,validated_data):
        print("$")
        print(validated_data)
        album = Album.objects.get(validated_data.pop("album"))
        Track.object.create(album = album,**validated_data)

class TrackSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['title','duration','genre']
        # fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    # album_track is the name of the related field
    # album_track = serializers.StringRelatedField(many=True)
    # album_track = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # view_name means url-path name
    # album_track = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='trackdetail')
    # album_track = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    # track_url = serializers.HyperlinkedIdentityField(view_name='trackdetail')
    album_track = TrackSerializer2(many=True,required=False)
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=False,queryset=User.objects.all())
    class Meta:
        model = Album
        fields = ['album_name','artist','user','album_track']

    def create(self,validated_data):
        try:
            with transaction.atomic():
                print("Here",validated_data)
                track_data = validated_data.pop('album_track',False)
                user = validated_data.pop('user')
                album = Album.objects.create(user=user,**validated_data)
                print(validated_data)
                print(track_data)
                if track_data != False:
                    for i in track_data:
                        Track.objects.create(album=album,**track_data[0])
                return album
        except Exception as e:
            error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error)




class AlbumSerializer2(serializers.ModelSerializer):
    album_track = TrackSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['album_name','artist','album_track']

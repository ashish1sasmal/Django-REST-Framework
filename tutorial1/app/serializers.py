from .models import Student

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset = Student.objects.all())
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = User
        fields = ('id','username','students')


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    rollno = serializers.IntegerField()
    marks = serializers.FloatField()
    branch = serializers.CharField(max_length=10)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,inst,validated_data):
        print(validated_data)
        inst.name = validated_data.get('name',inst.name)
        inst.rollno = validated_data.get('rollno',inst.rollno)
        inst.marks = validated_data.get('marks',inst.marks)
        inst.branch = validated_data.get('branch',inst.branch)
        inst.save()
        return inst

class StudentSerializer2(serializers.ModelSerializer):
    def clean_rollno(self):
        marks = self.cleaned_data['marks']
        if marks<33:
            raise Vaili
    class Meta:
        model = Student
        fields = ('id','name','rollno','marks','branch')

    # def update(self,inst,validated_data):
    #     print(validated_data)
    #     inst.name = validated_data.get('name',instance.name)
    #     inst.rollno = validated_data.get('rollno',instance.rollno)
    #     inst.marks = validated_data.get('marks',instance.marks)
    #     inst.branch = validated_data.get('branch',instance.branch)
    #     inst.save()
    #     return inst

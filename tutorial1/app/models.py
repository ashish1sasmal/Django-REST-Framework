from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.IntegerField()
    marks = models.FloatField()
    branch = models.CharField(max_length=10)
    user = models.ForeignKey(User,related_name='student', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}_{self.rollno}"

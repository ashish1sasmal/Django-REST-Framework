from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.IntegerField()
    marks = models.FloatField()
    branch = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}_{self.rollno}"

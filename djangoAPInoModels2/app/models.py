from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=40)
    rollno = models.IntegerField()
    marks = models.IntegerField()
    gf = models.CharField(max_length=40)
    bf = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}_{self.rollno}"

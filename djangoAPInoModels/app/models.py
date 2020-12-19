from django.db import models

# Create your models here.

class Employee(models.Model):
    enum = models.IntegerField()
    ename= models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.enum}_{self.ename}"
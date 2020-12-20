from django.contrib import admin

# Register your models here.
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','marks','branch']


admin.site.register(Student,StudentAdmin)

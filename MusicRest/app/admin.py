from django.contrib import admin

# Register your models here.
from .models import *

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(Album)
admin.site.register(Track)

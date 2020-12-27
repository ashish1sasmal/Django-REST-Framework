"""MusicRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

from rest_framework.authtoken import views as tokenviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/<int:pk>',views.AlbumCbv.as_view()),
    path('track/<int:pk>',views.TrackCbv.as_view()),
    path('api/<int:pk>',views.trackdetail,name='trackdetail'),

]
urlpatterns += [
    path('api-token-auth/', views.CustomAuthToken.as_view())
]

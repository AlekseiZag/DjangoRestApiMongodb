from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'^', include('tutorials.urls')),
]

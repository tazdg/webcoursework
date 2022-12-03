from django.contrib import admin
from django.urls import path, include
from mainapp.views import helloworld


urlpatterns = [
    path('',helloworld),
]

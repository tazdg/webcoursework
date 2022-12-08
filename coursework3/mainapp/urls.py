from django.contrib import admin
from django.urls import path, include
from mainapp.views import helloworld, login, items_api


urlpatterns = [
    path('',helloworld),
    path('login/',login),
    path('api/items/', items_api),
]

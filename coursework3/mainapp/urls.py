from django.contrib import admin
from django.urls import path, include
from mainapp.views import helloworld, items_api, login_view, signup_view, logout_view


urlpatterns = [
    path('',helloworld),
    # path('login/',login),
    # path('login/',login_view),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('api/items/', items_api),
    path('api/item/<int:item_id>/', items_api, name="item api"),
]

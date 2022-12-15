from django.contrib import admin
from django.urls import path, include
from mainapp.views import helloworld, items_api, login_view, signup_view, logout_view, questionanswers_api, questionanswer_api


urlpatterns = [
    path('',helloworld),
    # path('login/',login),
    # path('login/',login_view),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),



    path('api/questionanswers/', questionanswers_api),
    path('api/questionanswer/<int:questionanswer_id>/',questionanswer_api),
    path('api/items/', items_api, name='items'),
    # path('api/uploadimage/', upload_image, name='uploadimage api'),
]

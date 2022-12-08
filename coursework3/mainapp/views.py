from django.shortcuts import render
from django.http import HttpResponse
from mainapp.models import Recipe
# Create your views here.

def helloworld(request):
    return render(request, 'mainapp/index.html', {
        'name': 'Auction Genie',
        'recipies': Recipe.objects.all(),
    })

def login(request):
    return render(request, 'mainapp/login.html', {
        'name': 'Login Page',
        
    })

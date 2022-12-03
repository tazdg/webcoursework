from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloworld(request):
    return render(request, 'mainapp/index.html', {
        'name': 'Auction Genie',
    })

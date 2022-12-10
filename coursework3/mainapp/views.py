from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from mainapp.models import Recipe, Item
# Create your views here.

def helloworld(request):
    return render(request, 'mainapp/index.html', {
        'name': 'Auction Genie',
        'recipies': Recipe.objects.all(),
        'items': Item.objects.all(),
    })


def items_api(request: HttpRequest) -> HttpResponse:
    '''This method gets and posts to the list of scans'''
    if request.method == 'GET':
        return JsonResponse({
            'items': [
                item.to_dict()
                for item in Item.objects.all()
            ]
        })



def login(request):
    return render(request, 'mainapp/login.html', {
        'name': 'Login Page',
        
    })

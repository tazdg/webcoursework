import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpRequest, JsonResponse
from mainapp.models import Recipe, Item, User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import LoginForm, SignupForm

# Create your views here.


def helloworld(request):
    return render(request, 'mainapp/index.html', {
        'name': 'Auction Genie',
        'recipies': Recipe.objects.all(),
        'items': Item.objects.all(),
    })


@login_required
def items_api(request: HttpRequest) -> HttpResponse:
    '''This method gets and posts to the list of scans'''
    if request.method == 'GET':
        return JsonResponse({
            'items': [
                item.to_dict()
                for item in Item.objects.all()
            ]
        })

    if request.method == 'POST':
        POST = json.loads(request.body)
        print(POST)
        title = POST['title']
        description = POST['description']
        # image = POST['image']
        starting_price = POST['starting_price']
        date_ends = POST['date_ends']
        available = POST['available']
        newScan = Item.objects.create(title=POST['title'], description = POST['description'] ,starting_price = POST['starting_price'], date_ends = POST['date_ends'], available=POST['available'])
        return JsonResponse(newScan.to_dict())



# def login(request):
#     return render(request, 'mainapp/login.html', {
#         'name': 'Login Page',
        
#     })

def signup_view(request):
    '''
    Signup function
    Users creating an account
    '''

    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # create a new user
            new_user = User.objects.create(username=username)
            # set user's password
            new_user.set_password(password)
            new_user.save()
            # authenticate user
            # establishes a session, will add user object as attribute
            # on request objects, for all subsequent requests until logout
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request,'mainapp/redirect.html')

    return render(request, 'mainapp/signup.html', {'form': SignupForm})


def login_view(request):
    '''
    Login function
    Users logging into the app
    '''

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request,'mainapp/redirect.html')
                # return redirect('http://localhost:5173/')


            # failed authentication
            return render(request, 'error.html', {
                'error': 'User not registered. Sign up first.'
            })

        # invalid form
        return render(request, 'mainapp/login.html', {
            'form': form
        })

    return render(request, 'mainapp/login.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    # return redirect('mainapp:login')
    return JsonResponse({})



import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseBadRequest
from mainapp.models import Recipe, Item, User, QuestionAnswer
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import User
from .forms import LoginForm, SignupForm

# Create your views here.


def helloworld(request):
    return render(request, 'mainapp/index.html', {
        'name': 'Auction Genie',
        'recipies': Recipe.objects.all(),
        'items': Item.objects.all(),
    })


# @csrf_exempt
# @login_required
# def users_api(request):
#     if request.method == 'POST':



@csrf_exempt
@login_required
def items_api(request: HttpRequest) -> HttpResponse:
    '''This method gets and posts to the list of items'''
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
        newItem = Item.objects.create(title=POST['title'], description = POST['description'] ,starting_price = POST['starting_price'], date_ends = POST['date_ends'], available=POST['available'])
        return JsonResponse(newItem.to_dict())



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
            new_user = User.objects.create(username=username)
            new_user.set_password(password)
            new_user.save()
            # authenticate user + create session
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


@login_required
def questionanswers_api(request):
    user = request.user
    view = request.GET['view'] if 'view' in request.GET else user.username

    if request.method == 'POST':
        recip = User.objects.get(username=request.POST['recip'])
        public = request.POST['public'] == "yes"
        text = request.POST['message']
        QuestionAnswer.objects.create(
            sender=user,
            recip=recip,
            text=text,
            # public=public,
        )

    if user.username != view:
        view_user = get_object_or_404(User, username=view)
        questionanswers = user.questionanswers_with(view_user)
    else:
        questionanswers = user.questionanswers

    return JsonResponse({
        'questionanswers': [questionanswer.to_dict() for questionanswer in questionanswers]
    })


@login_required
def questionanswer_api(request, questionanswer_id):

    questionanswer = get_object_or_404(QuestionAnswer, id=questionanswer_id)

    if request.method == 'DELETE':
        # Check if user has permission to delete message
        user = request.user
        if questionanswer.sender == user or questionanswer.recip == user:
            questionanswer.delete()
            return JsonResponse({})

        return HttpResponseBadRequest("User does not have permission to delete message")

    return HttpResponseBadRequest("Invalid method")


# @login_required
# def upload_image(request):
#     item = request.user

#     if 'img_file' in request.FILES:
#         image_file = request.FILES['img_file']
#         item.image = image_file
#         item.save()
#         return HttpResponse()
#     else:
#         raise Http404('Image file not received')



# @login_required
# def questionanswers_view(request):
#     '''
#     Users messages page
#     This view uses Vue + Ajax requests
#     '''

#     user = request.user
#     view = request.GET['view'] if 'view' in request.GET else user.username

#     if user.username != view:
#         view_user = get_object_or_404(User, username=view)
#         profile = view_user.profile
#         questionanswers = user.questionanswers_with(view_user)
#     else:
#         profile = user.profile
#         questionanswers = user.questionanswers

#     vue_data = json.dumps({
#         'user': user.to_dict(),
#         'view': view,
#         'profile': profile.to_dict() if profile else None,
#         'questionanswers': [questionanswer.to_dict() for questionanswer in questionanswers],
#     })

#     return render(request, 'mainapp/api/questionanswers.html', {
#         'page': 'questionanswers',
#         'vue_data': vue_data,
#     })


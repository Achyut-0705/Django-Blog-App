from django.shortcuts import render, HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from .models import User as Client

# # Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            u = form.cleaned_data['username']
            try:
                user = Client.objects.get(username=u)
            except:
                return render(request, 'login.html', {'status_message': 'User does not exist', 'status_code': 0})
            
            if check_password(form.cleaned_data['password'], user.password):
                return HttpResponse('logged in')
            return render(request, 'login.html', {'status_message': 'Username or Password invalid', 'status_code': 0})
    return render(request, 'login.html',{'title': 'Login'})


def logout(request):
    pass

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            client = Client.objects.filter(username=username)
            if len(client) == 0:
                password1 = form.cleaned_data['password_1']
                password2 = form.cleaned_data['password_2']
                if password1 == password2:
                    p = make_password(password1)
                    Client.objects.create(username = username, password = p ).save()
                    return HttpResponse('user created successfully')
                return HttpResponse('password do not match')
            return HttpResponse('user exist')
        return HttpResponse('form not valid')
    return render(request, 'register.html',{'title': 'Register'})

def edit(request):
    return render(request, 'EditProfile.html',{'title': 'Profile Edit'})
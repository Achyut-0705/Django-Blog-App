from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm
from .models import User as Client

# # Create your views here.
def login(request):
    if request.method == 'POST':
        pass
    return render(request, 'login.html',{'title': 'Login'})


def logout(request):
    pass

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            client = Client.objects.filter(username=username)
            if len(client) == 0:
                password1 = form.cleaned_data['password_1']
                password2 = form.cleaned_data['password_2']
                if password1 == password2:
                    Client.objects.create(username=username,password=password1).save()
                    return HttpResponse('user created successfully')
                return HttpResponse('password do not match')
            return HttpResponse('user exist')
        return HttpResponse('form not valid')
    return render(request, 'register.html',{'title': 'Register'})
from .models import User, Post
from django.db import models
from django import forms

        
        
class SignUpForm(forms.Form):
    username = forms.CharField(max_length=25)
    password_1 = forms.CharField(max_length=20,widget=forms.PasswordInput )
    password_2 = forms.CharField(max_length=20,widget=forms.PasswordInput )
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput )
from .models import User, Post
from django.db import models
from django import forms

# class UserForm(ModelForm):
#     password1 = models.CharField(max_length=30)
#     password2 = models.CharField(max_length=30)
#     class Meta:
#         model = User
#         fields = ['username','password1','password2']
        
        
class UserForm(forms.Form):
    username = forms.CharField(max_length=25)
    # password_1 = forms.CharField(max_length=20,widget=forms.PasswordInput )
    # password_2 = forms.CharField(max_length=20,widget=forms.PasswordInput )
    password_1 = forms.CharField(max_length=20)
    password_2 = forms.CharField(max_length=20)
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        

from django.shortcuts import render
from users.models import Post
# Create your views here.
def home(request):
    return render(request,'home.html', { 'title': 'Home','posts': Post.objects.all() } )
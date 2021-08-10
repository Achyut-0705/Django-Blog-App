from django.urls import path, include
from . import views

app_name = 'Direct'

urlpatterns = [
    path('', views.home, name = 'Home'),
]

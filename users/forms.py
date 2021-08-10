from .models import User, Post
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
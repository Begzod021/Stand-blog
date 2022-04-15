from pyexpat import model
from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'tag', 'category']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'post']
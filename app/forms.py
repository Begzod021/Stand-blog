from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django import forms
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text', 'image', 'category']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'text', 'image', 'category', 'price_month', 'price', 'phone']

class ImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ['image', 'product', 'company']

from django import forms
from .models import User
from django.forms import  TextInput
from django.contrib.auth.forms import UserChangeForm
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password':TextInput(attrs={
                'type':'password',
                'id':'password',
                'name':'password',
                'placeholder':'Password'
            }),
            'username':TextInput(attrs={
                'type':'text',
                'name':'username',
                'id':'username',
                'placeholder':'Username'
            }),
            'email':TextInput(attrs={
                'type':'email',
                'id':'email',
                'name':'email',
                'placeholder':'Email'
            })
        }

class EditForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ['first_name', 'last_name', 'username', 'avatar','back_avatar']
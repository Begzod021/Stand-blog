from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm 
from django.forms import  TextInput, Textarea
from django import forms
from .models import *

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['username', 'email', 'password','category', 'companyname','is_comapny']

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
            }),
            'companyname':TextInput(attrs={
                'type':'text',
                'id':'companyname',
                'name':'companyname',
                'placeholder':'company name',
            }),
        }


class WorkerUserForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ['username',  'worker_blog', 'email','password1', 'password2','is_worker']

        widgets = {
            'password1':TextInput(attrs={
                'type':'password',
                'id':'password',
                'name':'password',
                'placeholder':'Password'
            }),
            'password2':TextInput(attrs={
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
            }),
            'companyname':TextInput(attrs={
                'type':'text',
                'id':'companyname',
                'name':'companyname',
                'placeholder':'company name',
            }),
        }






class CompanyEdit(UserChangeForm):
    class Meta(UserChangeForm):
        model = Company
        fields = ['first_name', 'last_name', 'username', 'companyname', 'category', 'logo','companyfile','logo_company',]
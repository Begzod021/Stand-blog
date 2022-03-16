from cgitb import text
import imp

from django import forms
from .models import  Comment
from django.forms import ModelForm, Textarea
from django import forms
from ckeditor.widgets import CKEditorWidget

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
        'text': Textarea(attrs={
            'name':'message',
            'rows':'5',
            'cols':'20',
            'placeholder':'Comment',
            'id':'message',
        })
    }
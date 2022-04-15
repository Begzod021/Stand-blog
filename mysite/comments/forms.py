from .models import  Comment
from django.forms import ModelForm, TextInput, EmailInput, Textarea
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
        'text': Textarea(attrs={
            'name':'message',
            'rows':'5',
            'placeholder':'Comment',
            'id':'message'
        })
    }
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import Messages


class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={
                'name': 'name',
                'id': 'name',
                'placeholder': 'Name'
            }),
            'email': TextInput(attrs={
                'name': 'email',
                'id': 'email',
                'placeholder': 'Email'
            }),
            'subject': TextInput(attrs={
                'name': 'subject',
                'id': 'subject',
                'placeholder': 'Subject'
            }),
            'message': Textarea(attrs={
                'name': 'message',
                'id': 'message',
                'placeholder': 'Message'
            })
        }

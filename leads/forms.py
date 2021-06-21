from django import forms
from .models import User, Contact


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        )


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name',
                  'title',
                  'company',
                  'phone',
                  'email',
                  'website',
                  'telegram',
                  'twitter_personal',
                  'twitter_brand',
                  'linkedin',
                  'birthday',
                  'address',
                  'status',
                  'relationship',
                  'notes'
                  ]


class MessageForm(forms.Form):
    Message = forms.CharField(max_length=255)

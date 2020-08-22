'''
from django.db import forms
from django.forms import ModelForm
from .models import Credentials

class SignUpForm(forms.ModelForm):


    class Meta:
        model = Credentials
        fields = ['name', 'password','email_address']

'''     
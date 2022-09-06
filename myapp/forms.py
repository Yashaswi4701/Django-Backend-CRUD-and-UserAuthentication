from dataclasses import field
from django import forms 
from .models import Members
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MembersForm(forms.ModelForm):
    class Meta:
        model=Members
        fields=['name','designation','description','image']
        
        
class SignupForm(UserCreationForm):
    email=forms.EmailField(max_length=60,help_text='Required. Add a valid email address')

    class Meta:
        model=User
        fields=['email','username']
        
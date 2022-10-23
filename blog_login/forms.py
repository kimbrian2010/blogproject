from dataclasses import fields
from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address')
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
        
class UserEditProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')
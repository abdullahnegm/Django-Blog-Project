from django import forms
from django.contrib.auth.models import User




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'passowrd1', 'passowrd2']



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password1']
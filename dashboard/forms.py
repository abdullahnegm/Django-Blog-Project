from django.forms import fields
from django import forms
from posts.models import Badwords, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from posts.models import Badwords, Category, Post


class BadwordsForm(forms.ModelForm):

    class Meta:
        model = Badwords
        fields = ('badword',)
        widgets = {
            'badword': forms.TextInput(attrs={'class': 'form-control'})
        }


class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserForm(UserCreationForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'placeholder': 'password'}),
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'placeholder': 'password'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'align': 'center', 'placeholder': 'UserName'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'align': 'center', 'placeholder': 'Email', 'required': True}),
        }


class PostsForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    image = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'btn btn-default btn-file w-100'}))
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': ''}), choices=(
        (category.id, category.name) for category in Category.objects.all()))

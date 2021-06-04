from django import forms
from django.forms import fields

from .models import Category

class postForm(forms.Form):

    title = forms.CharField()
    content = forms.CharField( widget=forms.Textarea())
    image = forms.ImageField()
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=((category.id ,category.name) for category in Category.objects.all()))

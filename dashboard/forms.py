from django import forms
from posts.models import Badwords , Category


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
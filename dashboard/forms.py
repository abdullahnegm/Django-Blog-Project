from django import forms
from posts.models import Badwords


class BadwordsForm(forms.ModelForm):

    class Meta:
        model = Badwords
        fields = ('badword',)
        widgets = {
            'badword': forms.TextInput(attrs={'class': 'form-control'})
        }

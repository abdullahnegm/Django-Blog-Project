from django import forms


class commentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())

    
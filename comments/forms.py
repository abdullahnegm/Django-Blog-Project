from django import forms


class commentForm(forms.Form):
    content = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'w-100 form-control' , 'placeholder':'Say something...'})
        )

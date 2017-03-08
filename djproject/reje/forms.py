from django import forms

class logowanie(forms.Form):
    twoja_nazwa = forms.CharField(label='Login: ', max_length=20)

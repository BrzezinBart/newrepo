from django import forms

class logowanie(forms.Form):
    your_name = forms.CharField(label='Twój login', max_length=20)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


from django import forms

class logg(forms.Form):
 username = forms.CharField(label='Twój login \r', max_length=100)
 password = forms.CharField(label='\n\r Twoje haslo', max_length=100)
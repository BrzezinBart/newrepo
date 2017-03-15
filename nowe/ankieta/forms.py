from django import forms

class AnkietaForm(forms.Form):
    nazwa = forms.CharField()
from django.shortcuts import render
from django.forms import ModelChoiceField
from ankieta.models import Choice
from django import forms

from rejestracja.models import Usr


class mojModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "Opcja : %s" % obj.nazwa

class Meta:
    model = Usr
    fields = ('username')

class VoteForm(forms.Form):
    wybor = mojModelChoiceField(queryset=Choice.objects.all())
    username = forms.CharField()
    data_z = forms.DateField()
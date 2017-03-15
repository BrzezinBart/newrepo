from django.shortcuts import render
from django.forms import ModelChoiceField, ModelChoiceField
from ankieta.models import Choice, AnkietaModel
from django import forms

from rejestracja.models import Usr
from wybor.forms import MyModelChoiceField


class mojModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "Opcja : %s" % obj.nazwa

class Meta:
    model = Usr
    fields = ('username')

class VoteForm(forms.Form):
    wybor = mojModelChoiceField(queryset=Choice.objects.all(), widget=forms.RadioSelect)


from django import forms
from django.db import models

from ankieta.models import AnkietaModel


class AnkietaForm(forms.Form):
    nazwa = forms.CharField()
    data_z = forms.DateField()

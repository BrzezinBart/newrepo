from django import forms
from django.db import models

from ankieta.models import Ankieta_model


class Ankieta_form (forms.Form):
    nazwa = forms.CharField()
    data_z = forms.DateField()




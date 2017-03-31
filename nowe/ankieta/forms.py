from django import forms
from datetime import datetime, timedelta
from django.contrib.admin.widgets import AdminDateWidget

from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import SelectDateWidget


class AnkietaForm(forms.Form):
    nazwa = forms.CharField()
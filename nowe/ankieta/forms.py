from django import forms
from datetime import datetime, timedelta

from django.core.validators import MaxValueValidator, MinValueValidator


class AnkietaForm(forms.Form):
    nazwa = forms.CharField()
    data_w = forms.IntegerField(help_text=' <br><center>(w dniach np. "3") domyślnie 7 dni.', label='Ważność ankiety', required=False, validators=[MaxValueValidator(14), MinValueValidator(1,message='Ważność ankiety jako wartość ujemna ??')])
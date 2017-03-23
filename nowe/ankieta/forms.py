from django import forms
from datetime import datetime, timedelta

class AnkietaForm(forms.Form):
    nazwa = forms.CharField()
    data_w = forms.IntegerField(help_text=' <br><center>(w dniach np. "3") domyślnie 7 dni.', label='Ważność ankiety', required=False)
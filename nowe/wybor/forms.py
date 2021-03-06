from django import forms
from django.forms import ModelChoiceField
from ankieta.models import AnkietaModel

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.nazwa

class ChoiceForm(forms.Form):
    nazwa = forms.CharField()
    link = forms.URLField(required = False)


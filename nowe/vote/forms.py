from django.forms import ModelChoiceField
from ankieta.models import Choice
from django import forms

class mojModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "Opcja : %s" % obj.nazwa

class VoteForm(forms.Form):
    wybor = mojModelChoiceField(queryset=Choice.objects.all(), widget=forms.RadioSelect, empty_label=None)


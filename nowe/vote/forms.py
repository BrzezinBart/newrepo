from django.forms import ModelChoiceField
from ankieta.models import Choice, AnkietaModel
from django import forms
from django.forms import formset_factory

class mojModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s: %s" % (AnkietaModel.objects.get(id=obj.ankieta_id).nazwa,obj.nazwa)


class VoteForm(forms.Form):
    wybor = mojModelChoiceField(queryset=Choice.objects.all(), widget=forms.RadioSelect, empty_label=None)
VoteFormSet = formset_factory(VoteForm)



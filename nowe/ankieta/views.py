from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from ankieta.models import AnkietaModel
from django.db import IntegrityError

from ankieta.forms import AnkietaForm



def survAdd(request):
    if request.method == 'POST':
        ankieta = AnkietaForm(request.POST)
        if ankieta.is_valid():
            nazwa = ankieta.cleaned_data['nazwa']
            data_z = ankieta.cleaned_data['data_z']
            ankieta_add = AnkietaModel.objects.create(nazwa=nazwa, data_z=data_z)
            return redirect('succes_a')
    else:
        ankieta = AnkietaForm()
    c = dict(form=AnkietaForm)
    c.update(csrf(request))
    return render_to_response("surv_add.html", c)



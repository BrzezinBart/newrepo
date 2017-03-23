from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf

from ankieta import forms
from ankieta.models import AnkietaModel
from ankieta.forms import AnkietaForm
from datetime import datetime, time, timedelta


@login_required(login_url='/login/')
def survAdd(request):
    if request.method == 'POST':
        ankieta = AnkietaForm(request.POST)
        if ankieta.is_valid():
            nazwa = ankieta.cleaned_data['nazwa']
            autor = request.user
            data_w = ankieta.cleaned_data['data_w']
            date = datetime.today()+timedelta(days=data_w)
            ankieta_add = AnkietaModel.objects.create(nazwa=nazwa, autor=autor, data_w=date)

            return redirect('succes_a')
    else:
        ankieta = AnkietaForm()
    c = dict(form=AnkietaForm)
    c.update(csrf(request))
    c.update({'lista':AnkietaModel.objects.all()})
    return render(request,'surv_add.html', c)







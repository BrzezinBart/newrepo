from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from ankieta.models import AnkietaModel
from ankieta.forms import AnkietaForm

@login_required(login_url='/login/')
def survAdd(request):
    if request.method == 'POST':
        ankieta = AnkietaForm(request.POST)
        if ankieta.is_valid():
            nazwa = ankieta.cleaned_data['nazwa']
            ankieta_add = AnkietaModel.objects.create(nazwa=nazwa)
            return redirect('succes_a')
    else:
        ankieta = AnkietaForm()
    c = dict(form=AnkietaForm)
    c.update(csrf(request))
    c.update({'lista':AnkietaModel.objects.all()})
    return render(request,'surv_add.html', c)







from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from ankieta.models import Ankieta_model
from django.db.utils import IntegrityError

from ankieta.forms import Ankieta_form


def surv_add(request):
    if request.method == 'POST':
        Ankieta = Ankieta_form(request.POST)
        if Ankieta.is_valid():
            try:
                nazwa = Ankieta.cleaned_data['nazwa']
            except:
                IntegrityError
            data_z = Ankieta.cleaned_data['data_z']
            Ankieta_add = Ankieta_model.objects.create(nazwa=nazwa, data_z=data_z)
            return redirect('succes')
    else:
        Ankieta = Ankieta_form()
    c = dict(form=Ankieta_form)
    c.update(csrf(request))
    return render_to_response("surv_add.html", c)


#for ankieta in Ankieta_model.objects.all():
#    print(ankieta.nazwa)


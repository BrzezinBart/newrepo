from django.shortcuts import redirect, render_to_response
from django.template.context_processors import csrf
from ankieta.models import Choice
from wybor.forms import ChoiceForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def choiceAdd(request):
    if request.method == 'POST':
        choice = ChoiceForm(request.POST)
        if choice.is_valid():
            ankieta = choice.cleaned_data['ankieta']
            nazwa = choice.cleaned_data['nazwa']
            autor = choice.cleaned_data['autor']
            link = choice.cleaned_data['link']
            choice_add = Choice.objects.create(nazwa=nazwa, autor=autor, link=link, ankieta=ankieta)
            return redirect('succes_a_d')
    else:
        ankieta = ChoiceForm()
    c = dict(form=ChoiceForm)
    c.update(csrf(request))
    c.update({'lista':Choice.objects.all()})
    return render_to_response("surv_add_choice.html", c)

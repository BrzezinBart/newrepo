from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render_to_response, render, get_object_or_404
from django.template.context_processors import csrf
from ankieta.models import Choice, AnkietaModel
from wybor.forms import ChoiceForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def choiceAdd(request,surv_id):
    if request.method == 'POST':
        choice = ChoiceForm(request.POST)
        if choice.is_valid():
            surv_id=(int(surv_id))
            nazwa = choice.cleaned_data['nazwa']
            autor = request.user
            link = choice.cleaned_data['link']
            choice_add = Choice.objects.create(nazwa=nazwa, autor=autor, link=link, ankieta_id=surv_id)
            return redirect('succes_a_d')
    else:
        ankieta = ChoiceForm()
    c = dict(form=ChoiceForm)
    c.update(surv_id=int(surv_id))
    c.update(csrf(request))
    c.update({'lista1':AnkietaModel.objects.all()})
    c.update({'lista':Choice.objects.all()})
    return render(request, template_name="surv_add_choice.html", context=c)

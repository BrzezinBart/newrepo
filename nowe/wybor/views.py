from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render_to_response, render, get_object_or_404
from django.template.context_processors import csrf
from ankieta.models import Choice, AnkietaModel
from wybor.forms import ChoiceForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

@login_required(login_url='/login/')
def choiceAdd(request,surv_id):
    error=None
    if request.method == 'POST':
        choice = ChoiceForm(request.POST)
        if choice.is_valid():
            surv_id=(int(surv_id))
            nazwa = choice.cleaned_data['nazwa']
            autor = request.user
            link = choice.cleaned_data['link']
            try:
                choice_add = Choice.objects.create(nazwa=nazwa, autor=autor, link=link, ankieta_id=surv_id)
            except IntegrityError:
                error = "Opcja o podanej nazwie już istnieje!"
            else:
                return redirect('voteAdd',surv_id)

    else:
        ankieta = ChoiceForm()
    c = dict(form=ChoiceForm)
    c.update(surv_id=int(surv_id))
    c.update(csrf(request))
    c.update({'error':error})
    c.update({'lista1':AnkietaModel.objects.all()})
    c.update({'lista':Choice.objects.all()})
    return render(request, template_name="surv_add_choice.html", context=c)

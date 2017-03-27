from datetime import datetime, time, timedelta
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render_to_response, render, get_object_or_404
from django.template.context_processors import csrf
from ankieta.models import Vote, AnkietaModel, Choice
from vote.forms import VoteForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def voteAdd(request,choice_id):
    error = None
    if request.method == 'POST':
        selected_option = request.POST.get('wybor')
        if selected_option is None:
            HttpResponseBadRequest('Nie istnieje')
        option = get_object_or_404(Choice, pk=int(selected_option))
        user_id = request.user
        try:
            vote_add = Vote.objects.create(wybor=option, Usr=user_id)
        except IntegrityError:
            error = "Nie wolno głosować dwa razy na to samo"
        else:
            return redirect('succes_v_a',)

    c=(csrf(request))
    c.update({'votes':Vote.objects.all()})
    c.update(cid=int(choice_id))
    c.update({'lista1': Choice.objects.all()})
    c.update({'lista': AnkietaModel.objects.all()})
    c.update({'error': error})
    return render(request, template_name='vote_add.html', context=c)


def countVotes(request):

    choices=Choice.objects.all()
    surveys=AnkietaModel.objects.all()
    x={'choices':choices}
    x.update({'survs':surveys})
    x.update({'dzis':datetime.today()})
    return render(request, template_name='votes.html', context=x)








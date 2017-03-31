from datetime import datetime, time, timedelta, date
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
        selected_option = request.POST.getlist('wybor1')
        if selected_option is None:
            HttpResponseBadRequest('Nie istnieje')
        user_id = request.user
        try:
            for item in selected_option:
                option = get_object_or_404(Choice, pk=int(item))
                vote_add = Vote.objects.create(wybor_id=int(item), Usr=user_id)
        except IntegrityError:
            error = "Nie wolno głosować dwa razy na to samo"
        else:
            return redirect('choice_id/countVotes')

    c=(csrf(request))
    c.update({'votes':Vote.objects.all()})
    c.update(cid=int(choice_id))
    c.update({'lista1': Choice.objects.filter(ankieta_id=int(choice_id))})
    c.update({'lista': AnkietaModel.objects.all()})
    c.update({'error': error})
    c.update({'dzis':datetime.today()})
    c.update({'a':AnkietaModel.objects.get(id=int(choice_id))})
    return render(request, template_name='vote_add.html', context=c)


def countVotes(request,choice_id):

    x={'choices':Choice.objects.all()}
    x.update(cid=choice_id)
    x.update({'dzis':datetime.today()})
    x.update({'survs':AnkietaModel.objects.filter(id=int(choice_id))})
    return render(request, template_name='votes.html', context=x)








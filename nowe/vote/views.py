from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from ankieta.models import AnkietaModel
from ankieta.models import Vote
from vote.forms import VoteForm
from rejestracja.models import Usr



def voteAdd(request):
    if request.method == 'POST':
        vote = VoteForm(request.POST)
        if vote.is_valid():
            wybor = vote.cleaned_data['wybor']
            user_id = request.user
            vote_add = Vote.objects.create(wybor=wybor, Usr=user_id)
            return redirect('succes_a_d')
        else:
            print(vote.errors)
            print(vote.cleaned_data)
    else:
        vote = VoteForm()
    c = dict(form=VoteForm)
    c.update(csrf(request))
    return render_to_response("vote_add.html", c)


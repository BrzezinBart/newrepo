from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from ankieta.models import AnkietaModel
from ankieta.models import Vote
from vote.forms import VoteForm

def voteAdd(request):
    if request.method == 'POST':
        vote = VoteForm(request.POST)
        if vote.is_valid():
            wybor = vote.cleaned_data['wybor']
            username = vote.cleaned_data['username']
            data = vote.cleaned_data['data_z']
            vote_add = Vote.objects.create(wybor=wybor, Usr=username , data=data)
            return redirect('succes_a_d')
    else:
        vote = VoteForm()
    c = dict(form=VoteForm)
    c.update(csrf(request))
    return render_to_response("surv_add_choice.html", c)

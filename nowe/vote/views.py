from django.shortcuts import redirect, render_to_response
from django.template.context_processors import csrf
from ankieta.models import Vote
from vote.forms import VoteForm
from django.contrib.auth.decorators import login_required
from ankieta.models import AnkietaModel

@login_required(login_url='/login/')
def voteAdd(request):
    if request.method == 'POST':
        vote = VoteForm(request.POST)
        if vote.is_valid():
            vote.get_user()
            wybor = vote.cleaned_data['wybor']
            user_id = request.user
            vote_add = Vote.objects.create(wybor=wybor, Usr=user_id)
            return redirect('succes_v_a')
        else:
            print(vote.errors)
            print(vote.cleaned_data)
    else:
        vote = VoteForm()
    c = dict(voteForm=VoteForm)
    c.update(csrf(request))
    return render_to_response("vote_add.html", c)


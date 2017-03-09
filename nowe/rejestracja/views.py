from django.shortcuts import render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from .forms import reje1

def reje(request):
    if request.method == 'POST':
        form1 = reje1(request.POST)
        if form1.is_valid():
            user = form1.save()  # save user to db
            return redirect('succes')
    else:
        form1 = reje1()
    c = dict(form=form1)
    c.update(csrf(request))
    return render_to_response("register.html", c)

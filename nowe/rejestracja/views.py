from django.shortcuts import render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from rejestracja.forms import reg_form

def reg_view(request):
    if request.method == 'POST':
        form1 = reg_form(request.POST)
        if form1.is_valid():
            user = form1.save()  # save user to db
            return redirect('succes')
    else:
        form1 = reg_form()
    c = dict(form=form1)
    c.update(csrf(request))
    return render_to_response("register.html", c)

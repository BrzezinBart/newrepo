from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import logg

def logowanie(request):

    if request.method == 'POST':

        form = logg(request.POST)

        if form.is_valid():

            return HttpResponseRedirect('/')

    else:
        form = logg()

    return render(request, '1.html', {'form': form})
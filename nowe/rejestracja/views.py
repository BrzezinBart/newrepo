from .forms import reje
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
import django.shortcuts
from django.contrib.auth.forms import UserCreationForm


class rejestracja(FormView):
    template_name = 'register.html'
    form_class = reje
    success_url = '/'

def rejestracja1(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if form.is_valid():
                user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password1'])
                user.save()
                return render_to_response('/')  # Redirect after POST
            else:
                form = UserCreationForm()  # An unbound form

        return render_to_response('register.html', {
            'form': form,
        }, context_instance=RequestContext(request))
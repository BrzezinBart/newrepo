from rejestracja.forms import UserCreationForm
from django.views.generic.edit import FormView


class Rejestracja(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = 'register.html'

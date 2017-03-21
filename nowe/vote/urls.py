from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from rejestracja.views import reg_view
from ankieta.views import survAdd
from wybor.views import choiceAdd
from vote.views import voteAdd , detail


urlpatterns = [
    url(r'^$', detail, name='index'),
    url(r'^vote_add/(?P<choice_id>[0-9])', detail, name='detail')

]
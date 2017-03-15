from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from rejestracja.views import reg_view
from ankieta.views import survAdd
from wybor.views import choiceAdd
from vote.views import voteAdd

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^register/$', reg_view, name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^succes/', TemplateView.as_view(template_name='succes.html'), name='succes'),
    url(r'^surv_add/', survAdd, name='surv_add'),
    url(r'^surv_succ/', survAdd, name='surv_succ'),
    url(r'^succes_a/', TemplateView.as_view(template_name='succes_a.html'), name='succes_a'),
    url(r'^succes_a_d/', TemplateView.as_view(template_name='succes_a_c.html'), name='succes_a_d'),
    url(r'^vote_add', voteAdd, name='vote_add'),
    url(r'^surv_add_choice/', choiceAdd, name='surv_add_choice'),
]

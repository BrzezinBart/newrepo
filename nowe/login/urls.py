from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from rejestracja.views import reg_view
from ankieta.views import surv_add
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^register/$', reg_view, name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^succes/', TemplateView.as_view(template_name='succes.html'), name='succes'),
    url(r'^surv_add/', surv_add, name='surv_add'),
    url(r'^surv_succ/', surv_add, name='surv_succ')
]

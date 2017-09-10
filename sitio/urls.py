from django.contrib.auth.views import LoginView
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^productos/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^picadas/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contacto/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^nosotros/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]

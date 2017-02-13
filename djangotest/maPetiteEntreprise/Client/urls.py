from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from Client import views

admin.autodiscover()

urlpatterns = [
    url(r'^$','Client.views.home', name='home'),
    url(r'^lol/$', 'Client.view.liste_produits', name='liste_produits'),
]

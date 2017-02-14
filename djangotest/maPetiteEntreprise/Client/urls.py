from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from Client import views

admin.autodiscover()

urlpatterns = [
    url(r'^$','Client.views.home_client', name='home_client'),
    url(r'^liste_produits/', 'Client.views.liste_produits_client', name='liste_produits_client'),
    url(r'^ajout_produit/', 'Client.views.ajout_produit_client', name='ajout_produit_client'),
]

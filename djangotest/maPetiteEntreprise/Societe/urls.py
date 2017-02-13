from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from Societe import views

admin.autodiscover()

urlpatterns = [
    url(r'^$','Societe.views.home_societe', name='home_societe'),
    url(r'^liste_produits/', 'Societe.views.liste_produits', name='liste_produits'),
]

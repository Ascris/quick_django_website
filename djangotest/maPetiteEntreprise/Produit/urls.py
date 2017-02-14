from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from Produit import views
from Client import views

admin.autodiscover()

urlpatterns = [
    url(r'^$','Produit.views.home_produit', name='home_produit'),
    url(r'^delete$','Produit.views.delete', name='delete'),
]

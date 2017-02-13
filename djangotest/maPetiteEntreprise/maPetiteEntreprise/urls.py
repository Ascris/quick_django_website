"""maPetiteEntreprise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$','maPetiteEntreprise.views.home', name='home'),
    url(r'^login/$','django.contrib.auth.views.login', name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout', name='logout'),
    url(r'^access_forbidden/$','maPetiteEntreprise.views.access_forbidden', name='access_forbidden'),
    url(r'^contact/','maPetiteEntreprise.views.contact', name='contact'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lol/', include('Client.urls')),
    url(r'^client/','Client.views.home', name='home_client'),
    url(r'^produit/','Produit.views.home', name='home_produit'),
    url(r'^societe/','Societe.views.home', name='home_societe'),
    url(r'^liste_produits/','maPetiteEntreprise.views.liste_produits', name='liste_produits'),
    url(r'^archives/','maPetiteEntreprise.views.recherche_archives', name='recherche'),
    url(r'^credits/','maPetiteEntreprise.views.credits', name='credits'),
    url(r'^liste_clients/','maPetiteEntreprise.views.liste_clients', name='liste_clients'),
]

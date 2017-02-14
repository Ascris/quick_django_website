from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth

from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf

from Client.models import Client
from Produit.models import Produit

from form import MyRegistrationForm

def home_client(request):
    return render(request, 'home_client.html')

#def register(request):
 #   user= User.objects.create_user('ascris', 'as@cris.fr', 'ascris_mdp')
  #  user.save()
   # return render(request, 'register.html')

def liste_produits_client(request):
    p = Produit.objects.create(nom='P1', prix='50')
    c= Client.objects.create(nom='GARNIER', prenom='Antoine', age= '16', courriel='lol@dez.fr')
    c.produits.add(p)
    mes_produits= c.produits
    return render(request, 'liste_produits_client.html', {'mes_produits':mes_produits})

def ajout_produit_client(request):
    p = Produit.objects.create(nom='Subnautica', prix='30')
    c= Client.objects.create(nom='GARNIER', prenom='Antoine', age= '16', courriel='lol@MOI.fr')
    c.produits.add(p)
    mes_produits= c.produits
    return render(request, 'ajout_produit_client.html', {'mes_produits':mes_produits})

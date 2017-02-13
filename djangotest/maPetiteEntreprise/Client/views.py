from django.shortcuts import render
from django.conf import settings

from Client.models import Client
from Produit.models import Produit

def home_client(request):
    return render(request, 'home_client.html')

def liste_produits_client(request):
    p = Produit.objects.create(nom='P1', prix='50')
    c= Client.objects.create(nom='GARNIER', prenom='Antoine', age= '16', courriel='lol@dez.fr')
    c.produits.add(p)
    mes_produits= c.produits
    return render(request, 'liste_produits_client.html', {'mes_produits':mes_produits})


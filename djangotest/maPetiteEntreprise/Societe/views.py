from django.shortcuts import render
from django.conf import settings

from Societe.models import Societe
from Produit.models import Produit

def home_societe(request):
    return render(request, 'home_societe.html')

def ajout_produit(request):
    p= Produit(nom='Chocolat')
    p.save()
    p.societes.add(this)

def liste_produits(request):
    mes_produits= Societe.produits.get(all)
    return render(request, 'liste_produits.html', {'mes_produits':mes_produits})


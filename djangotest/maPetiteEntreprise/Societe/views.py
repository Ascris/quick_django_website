from django.shortcuts import render
from django.conf import settings

from Produit.models import Produit

def home(request):
    return render(request, 'home_societe.html')

def ajout_produit(request):
    p= Produit(nom='Chocolat')
    p.save()
    p.societes.add(this)

def liste_produits(request):
    mes_produits= this.produits
    return render(request, 'liste_produits.html', {'mes_produits':mes_produits})


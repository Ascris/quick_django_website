from django.shortcuts import render
from django.conf import settings

from Produit.models import Produit

def home_produit(request):
    return render(request, 'home_produit.html')

def ajout(request):
    Produit.objects.create(nom="PS4", prix="5")
    return render(request, 'liste_produits.html')

def delete(request):
    Produit.objects.filter(nom='Subnautica').delete()
    return render(request, 'liste_produits.html')

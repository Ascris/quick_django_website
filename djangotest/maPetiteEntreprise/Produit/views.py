from django.shortcuts import render
from django.conf import settings

from Produit.models import Produit

def home_produit(request):
    return render(request, 'home_produit.html')

def delete(request):
    Produit.objects.filter(nom='P1').delete()
    return render(request, 'liste_produits.html')

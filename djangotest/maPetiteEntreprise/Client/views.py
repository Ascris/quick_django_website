from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, 'home_c.html')

def liste_produits(request):
    return render(request, 'liste_produits.html')

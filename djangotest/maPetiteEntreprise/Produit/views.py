from django.shortcuts import render
from django.conf import settings

def home_produit(request):
    return render(request, 'home_produit.html')

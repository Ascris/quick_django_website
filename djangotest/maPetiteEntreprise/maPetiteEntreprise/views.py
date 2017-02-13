from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

from Produit.models import Produit
from Client.models import Client
from Societe.models import Societe

def home(request):
    n=5
    return render(request, 'home.html', {'parametre':n})

def contact(request):
    createur="etudiant"
    return render(request, 'contact.html', {'createur':createur})

@login_required(login_url='access_forbidden')
def liste_clients(request):
    mes_clients= Client.objects.all()
    return render(request, 'liste_clients.html', {'liste_clients':mes_clients})

@login_required(login_url='access_forbidden')
def liste_produits(request):
    mes_produits= Produit.objects.all()
    return render(request, 'liste_produits.html', {'mes_produits':mes_produits})

@login_required(login_url='access_forbidden')
def recherche_archives(request):
    return render(request, 'recherche_archives.html')

def credits(request):
    return render(request, 'credits.html')

def access_forbidden(request):
    return render(request, 'error/access_forbidden.html')

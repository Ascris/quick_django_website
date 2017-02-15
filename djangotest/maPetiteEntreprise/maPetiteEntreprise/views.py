from django.shortcuts import render
from django.shortcuts import render_to_response

from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.core.context_processors import csrf

from maPetiteEntreprise.forms import UserCreateForm

from Produit.models import Produit
from Client.models import Client
from Societe.models import Societe

from cart.cart import Cart

def home(request):
    n=5
    return render(request, 'home.html', {'parametre':n})

def register(request):
     if request.method == 'POST':	
         form = UserCreateForm(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/register/complete')
     else:
         form = UserCreateForm()
     token = {}
     token.update(csrf(request))
     token['form'] = form
     return render_to_response('registration/register.html', token)

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')

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

#Cart functions
@login_required
def add_to_cart(request, product_id):
    product = Produit.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.prix)
    return render(request, 'cart.html', dict(cart=Cart(request)))

@login_required
def remove_from_cart(request, product_id):
    product = Produit.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

@login_required
def get_cart(request):
    return render(request, 'cart.html', dict(cart=Cart(request)))

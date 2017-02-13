from django.db import models
#from Produit.models import Produit
#from Client.models import Client

# Create your models here.

class Societe(models.Model):
    nom= models.CharField(max_length=1024)
    directeur= models.CharField(max_length=1024)
    courriel= models.EmailField()
    date_creation= models.DateTimeField()
#    clients= models.ManyToManyField(Client)
#    produits= models.ManyToManyField(Produit)

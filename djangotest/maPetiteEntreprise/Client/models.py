from django.db import models
from Produit.models import Produit

# Create your models here.

class Client(models.Model):
    nom= models.CharField(max_length=1024)
    prenom= models.CharField(max_length=1024)
    age= models.IntegerField()
    courriel= models.EmailField()
    date_inscription= models.DateTimeField()
    produits= models.ManyToManyField(Produit)

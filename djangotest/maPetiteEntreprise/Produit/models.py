from django.db import models
from Societe.models import Societe

# Create your models here.

class Produit(models.Model):
    nom= models.CharField(max_length=1024)
    date_creation= models.DateTimeField()
    prix= models.IntegerField()
    societes= models.ManyToManyField(Societe)

from django.db import models


from rejestracja.models import Usr

# Create your models here.
class AnkietaModel(models.Model):
    nazwa = models.CharField(unique=True, null=False, max_length=50)
    data_z = models.DateField(auto_now=True)

class Choice(models.Model):
    autor = models.CharField(max_length=50)
    nazwa = models.CharField(unique=True, null=False, max_length=50)
    link = models.URLField(unique=True, null=True)
    ankieta = models.ForeignKey('AnkietaModel')

class Vote(models.Model):
    wybor = models.ForeignKey('Choice')
    Usr = models.ForeignKey('rejestracja.Usr')
    data = models.DateField(auto_now=False)
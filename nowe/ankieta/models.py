from django.db import models
from rejestracja.models import Usr

# Create your models here.
class Ankieta:
    nazwa = models.CharField(unique=True, null=False)
    data_zakonczenia = models.DateField(auto_now=False)

class Choice:
    autor = models.CharField
    nazwa = models.CharField(unique=True, null=False)
    link = models.URLField(unique=True, null=True)
    id_ankiety = models.foreignkey('Ankieta')

class Vote:
    id_wyboru = models.foreignkey('Choice')
    id_Usr = models.foreignkey('Usr')
    data = models.DateField(auto_now=False)



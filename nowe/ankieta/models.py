from django.db import models
from datetime import datetime, timedelta

class AnkietaModel(models.Model):
    autor = models.ForeignKey('rejestracja.Usr')
    nazwa = models.CharField(unique=True, null=False, max_length=50)
    data_z = models.DateTimeField(auto_now=True)
    data_w = models.DateTimeField(default=datetime.today()+timedelta(days=7))
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.nazwa

class Choice(models.Model):
    autor = models.ForeignKey('rejestracja.Usr')
    nazwa = models.CharField(unique=True, null=False, max_length=50)
    link = models.URLField(null=True, blank=True)
    ankieta = models.ForeignKey('AnkietaModel')
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.nazwa

class Vote(models.Model):
    wybor = models.ForeignKey('Choice')
    Usr = models.ForeignKey('rejestracja.Usr')
    data = models.DateField(auto_now=True)
    class Meta:
        unique_together = ["wybor", "Usr"]


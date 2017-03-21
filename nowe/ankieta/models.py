from django.db import models

class AnkietaModel(models.Model):
    nazwa = models.CharField(unique=True, null=False, max_length=50)
    data_z = models.DateField(auto_now=True)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.nazwa

class Choice(models.Model):
    autor = models.CharField(max_length=50)
    nazwa = models.CharField(unique=True, null=False, max_length=50)
    link = models.URLField(unique=True, null=True)
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
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.wybor

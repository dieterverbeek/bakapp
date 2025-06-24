from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


from django.db import models

class ActieVanHetMoment(models.Model):
    titel = models.CharField(max_length=100)
    omschrijving = models.TextField()
    actief_tot = models.DateField()

    def __str__(self):
        return self.titel



class Offerte(models.Model):
    naam_contactpersoon = models.CharField(max_length=255)
    email = models.EmailField()
    aantal_personen = models.PositiveIntegerField()
    straat = models.CharField(max_length=255)  # Origineel adres (bijv. van de aanvrager)
    nummer = models.CharField(max_length=50)
    gemeente = models.CharField(max_length=255)
    event_adres = models.CharField(max_length=255)  # Extra veld voor het event adres
    telefoon = models.CharField(max_length=20)  # Nieuw veld voor telefoon
    naam_bedrijf = models.CharField(max_length=255)
    btw_nummer = models.CharField(max_length=50, blank=True, null=True)
    gewenste_datum = models.DateField()
    gewenste_tijd = models.TimeField()
    formule = models.CharField(max_length=50)
    extra_info = models.TextField(blank=True, null=True)
    afstand = models.FloatField()
    extra_kosten = models.DecimalField(max_digits=10, decimal_places=2)
    basis_prijs = models.DecimalField(max_digits=10, decimal_places=2)
    totaal_prijs = models.DecimalField(max_digits=10, decimal_places=2)
    korting = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_bevestigd = models.CharField(max_length=50, default="Nieuwe offerte")
    created_at = models.DateTimeField(auto_now_add=True)

    herinnering_verstuurd_op = models.DateTimeField(null=True, blank=True, verbose_name="Datum herinnering verstuurd")

    def __str__(self):
        return f"Offerte van {self.naam} - €{self.totaal_prijs}"



class Klant(models.Model):
    naam_contactpersoon = models.CharField(max_length=255)
    email = models.EmailField()
    straat = models.CharField(max_length=255)
    nummer = models.CharField(max_length=50)
    gemeente = models.CharField(max_length=255)
    telefoon = models.CharField(max_length=20)
    naam_bedrijf = models.CharField(max_length=255)
    btw_nummer = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.naam_contactpersoon} - {self.naam_bedrijf}"


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
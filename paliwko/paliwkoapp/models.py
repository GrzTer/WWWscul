from django.db import models
from django.db.models.fields import CharField


class Paliwko(models.Model):
    rodzaj_paliwa = models.CharField(max_length=255)
    cena = models.FloatField()

    def __str__(self): return f"{self.rodzaj_paliwa}: {self.cena}"
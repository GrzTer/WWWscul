from datetime import datetime

from django.db import models

class Samochody(models.Model):
    marka = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    rocznik = models.IntegerField()
    kolor = models.CharField(max_length=200)
    stan = models.CharField(max_length=200)
    def __str__(self): return f"{self.marka} {self.model} - rocznik: {self.rocznik}"

class Zamowienia(models.Model):
    klient = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)
    data_zamowienia= models.DateField(default=datetime.today)
    id_samochodu= models.ForeignKey(Samochody, on_delete=models.CASCADE)
    def __str__(self): return f"{self.data_zamowienia} {self.klient} {self.id_samochodu.marka} {self.id_samochodu.model}"
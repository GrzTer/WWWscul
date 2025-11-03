from django.db import models

class Kadra(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    stanowisko = models.CharField(max_length=100)
    def __str__(self): return f"{self.stanowisko} - {self.imie} {self.nazwisko}"


class Uslugi(models.Model):
    nazwa = models.CharField(max_length=100)
    cena = models.IntegerField()
    kadra_id = models.ForeignKey(Kadra, on_delete=models.CASCADE)
    def __str__(self): return f"{self.nazwa} - {self.kadra_id.imie} {self.kadra_id.nazwisko}"

from django.db import models

from django.db import models

class Uzytkownik(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    telefon = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Ogloszenia(models.Model):
    kategoria = models.PositiveSmallIntegerField()
    podkategoria = models.PositiveSmallIntegerField()
    tytul = models.CharField(max_length=100)
    tresc = models.TextField()
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)

    def __str__(self):
        return self.tytul

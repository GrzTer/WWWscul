from django.db import models

class Osoba(models.Model):
    login = models.CharField(max_length=20)
    haslo = models.CharField(max_length=20)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    def __str__(self):
        return (self.login, self.haslo, self.imie, self.nazwisko)
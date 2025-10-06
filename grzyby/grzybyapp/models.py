from django.db import models
from django.db.models import ForeignKey


class Rodzina(models.Model):
    nazwa = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nazwa

class Potrawy(models.Model):
    nazwa = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nazwa

class Grzyby(models.Model):
    nazwa = models.CharField(max_length=100)
    potoczna = models.CharField(max_length=100)
    jadalny = models.CharField(max_length=100)
    miesiac_zbierania = models.CharField(max_length=100)
    rodzina_id = models.ForeignKey(Rodzina, on_delete=models.CASCADE)
    potrawy = models.ForeignKey(Potrawy, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nazwa
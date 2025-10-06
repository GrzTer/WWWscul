from django.db import models

class Rodzina(models.Model):
    nazwa = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa

class Potrawy(models.Model):
    nazwa = models.CharField(max_length=100)
    def __str__(self):
        return self.nazwa

class Grzyby(models.Model):
    nazwa = models.CharField(max_length=100)
    potoczna = models.CharField(max_length=100)
    jadalny = models.CharField(max_length=50)
    miesiac_zbierania = models.CharField(max_length=100)
    rodzina_id = models.ForeignKey(Rodzina, on_delete=models.CASCADE)
    potrawy_id = models.ForeignKey(Potrawy, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nazwa} - nazwa potoczna {self.potoczna}, należy do {self.rodzina_id}"
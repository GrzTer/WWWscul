from django.db import models


class Prowadzacy(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    def __str__(self):
        return f"Prowadzący {self.imie} {self.nazwisko}"

class Uczen(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    klasa = models.CharField(max_length=100)
    def __str__(self):
        return f"Uczący się {self.imie} {self.nazwisko} z klasy {self.klasa}"

class Spotkania(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    prowadzacy = models.ForeignKey(Prowadzacy, on_delete=models.CASCADE)
    uczen = models.ForeignKey(Uczen, on_delete=models.CASCADE)
    def __str__(self):
        return f"Spotkanie {self.title} {self.date} o godzinie {self.start_time} z długością {self.duration}"
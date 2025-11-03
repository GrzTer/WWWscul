from django.db import models


class Pacjent(models.Model):
    nazwisko = models.CharField(max_length=50)
    imie = models.CharField(max_length=50)
    miasto = models.CharField(max_length=50, default="Białystok")
    ulica = models.CharField(max_length=50)
    wiek = models.IntegerField(default=18)

    def __str__(self):
        # return f"Pacjent {self.nazwisko, self.imie} zamieszkały w {self.miasto} na ulicy {self.ulica}, ma lat {self.wiek}"
        return f"{self.nazwisko} { self.imie}"


class Wizyta(models.Model):
    date = models.DateField()
    zalecenia = models.CharField(max_length=255)
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE)

    def __str__(self):
        # return f"Wizyta dnia {self.date}, zalecenia {self.zalecenia}, dla pacjenta {self.pacjent}"
        return f"{self.date} {self.pacjent.nazwisko}"

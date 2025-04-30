from django.db import models


class Uzytkownik(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    telefon = models.PositiveIntegerField(default=000000000)
    email = models.EmailField()

    def __str__(self):
        # return f"Imie: {self.imie}, Nazwisko: {self.nazwisko}, Telefon: {self.telefon}, Email: {self.email}"
        return f"{self.imie} {self.nazwisko}"

class Ogloshenia(models.Model):
    kategoria = models.PositiveSmallIntegerField(default=0)
    podkategoria = models.PositiveSmallIntegerField(default=0)
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    uzytkownik_id = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)

    def __str__(self):
        # return f"Kategoria: {self.kategoria}, Podkategoria: {self.podkategoria}, Tytul: {self.tytul}, Treść: {self.tresc}, Użytkownik: {self.uzytkownik_id}"
        return f"{self.tytul} {self.tresc}"

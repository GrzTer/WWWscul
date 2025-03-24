from django.db import models


class Ryby(models.Model):
    nazwa = models.CharField(max_length=255)
    wystepowanie = models.CharField(max_length=255)
    styl_zycia = models.PositiveIntegerField()

    def __str__(self):
        return self.nazwa


class OkresOchronny(models.Model):
    od_miesiaca = models.IntegerField()
    do_miesiaca = models.IntegerField()
    wymiar_ochronny = models.IntegerField()
    ryby_id = models.ForeignKey(Ryby, on_delete=models.CASCADE)

    def __str__(self):
        return f"Okres ochronny dla {self.ryby.nazwa}"

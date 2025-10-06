from django.db import models


class Paint(models.Model):
    color = models.CharField(max_length=200)
    price = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Kolor: {self.color}; Cena: {self.price}; Pojemność: {self.capacity}"


class Painting(models.Model):
    id_room = models.IntegerField()
    id_wall = models.IntegerField()
    num_of_cans = models.IntegerField()
    id_paint = models.ForeignKey(Paint, on_delete=models.CASCADE)

    def __str__(self):
        return f"Id pomieszczenia: {self.id_room}; Id ściany: {self.id_wall}; Liczba puszek: {self.num_of_cans}; Id farby: {self.id_paint}"

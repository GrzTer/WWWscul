# Generated by Django 5.1.1 on 2024-10-02 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pacjent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nazwisko", models.CharField(max_length=50)),
                ("imie", models.CharField(max_length=50)),
                ("miasto", models.CharField(max_length=50)),
                ("ulica", models.CharField(default="Białystok", max_length=50)),
                ("wiek", models.IntegerField(default=18)),
            ],
        ),
        migrations.CreateModel(
            name="Wizyta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("zalecenia", models.CharField(max_length=255)),
                (
                    "pacjent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="GoodDoctor.pacjent",
                    ),
                ),
            ],
        ),
    ]

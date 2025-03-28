# Generated by Django 5.1.7 on 2025-03-24 22:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Uzytkownik",
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
                ("imie", models.CharField(max_length=50)),
                ("nazwisko", models.CharField(max_length=50)),
                ("telefon", models.PositiveIntegerField(default=0)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Ogloshenia",
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
                ("kategoria", models.PositiveSmallIntegerField(default=0)),
                ("podkategoria", models.PositiveSmallIntegerField(default=0)),
                ("tytul", models.CharField(max_length=200)),
                ("tresc", models.TextField()),
                (
                    "uzytkownik_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Oapp.uzytkownik",
                    ),
                ),
            ],
        ),
    ]

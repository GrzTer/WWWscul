# Generated by Django 5.1.1 on 2024-10-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("GoodDoctor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pacjent",
            name="miasto",
            field=models.CharField(default="Białystok", max_length=50),
        ),
        migrations.AlterField(
            model_name="pacjent",
            name="ulica",
            field=models.CharField(max_length=50),
        ),
    ]

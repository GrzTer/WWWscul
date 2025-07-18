# Generated by Django 5.2 on 2025-04-30 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_room', models.IntegerField()),
                ('id_wall', models.IntegerField()),
                ('num_of_cans', models.IntegerField()),
                ('id_paint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farbyapp.paint')),
            ],
        ),
    ]

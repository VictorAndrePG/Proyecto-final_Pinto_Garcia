# Generated by Django 4.2.7 on 2023-12-12 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFutbol', '0003_equipo_puntaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrenador',
            name='puntaje',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jugador',
            name='puntaje',
            field=models.IntegerField(default=0),
        ),
    ]

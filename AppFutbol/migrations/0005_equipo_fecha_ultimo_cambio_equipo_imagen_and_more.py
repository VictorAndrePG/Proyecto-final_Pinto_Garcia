# Generated by Django 4.2.7 on 2023-12-17 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppFutbol', '0004_entrenador_puntaje_jugador_puntaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='fecha_ultimo_cambio',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='equipo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='equipos/'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='usuario_creacion',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-30 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFutbol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Puntaje',
        ),
    ]

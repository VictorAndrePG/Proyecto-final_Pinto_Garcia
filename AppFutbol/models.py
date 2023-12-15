from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    puntaje = models.IntegerField(default=0)
    def __str__(self):
        return f"Equipo: {self.nombre} - Puntaje {self.puntaje} "


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    puntaje = models.IntegerField(default=0)

    def __str__(self):
        return f"Mostrando jugador: {self.nombre} {self.apellido} "


class Entrenador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    puntaje = models.IntegerField(default=0)
    def __str__(self):
        return f"Mostrando entrenador: {self.nombre} {self.apellido} "


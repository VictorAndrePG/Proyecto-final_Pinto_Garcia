from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=40)


    def __str__(self):
        return f"El equipo: {self.nombre} "


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)


    def __str__(self):
        return f"Mostrando jugador: {self.nombre} {self.apellido} "


class Entrenador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)


    def __str__(self):
        return f"Mostrando entrenador: {self.nombre} {self.apellido} "


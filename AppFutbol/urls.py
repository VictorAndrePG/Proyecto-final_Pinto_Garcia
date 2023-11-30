from django.urls import path
from AppFutbol.views import mostrar_equipos, agregar_equipo, mostrar_jugadores, mostrar_entrenadores, agregar_jugador, agregar_entrenador, seleccionar_categoria, busqueda_jugador, busqueda_entrenador, busqueda_equipo

urlpatterns = [
    path('mostrar_equipos/', mostrar_equipos, name='mostrar_equipos'),
    path('agregar_equipo/', agregar_equipo, name='agregar_equipo'),

    path('mostrar_jugadores/', mostrar_jugadores, name='mostrar_jugadores'),
    path('agregar_jugador/', agregar_jugador, name='agregar_jugador'),

    path('mostrar_entrenadores/', mostrar_entrenadores, name='mostrar_entrenadores'),
    path('agregar_entrenador/', agregar_entrenador, name='agregar_entrenador'),

    path('seleccionar_categoria/', seleccionar_categoria, name='seleccionar_categoria'),

    path('buscar_entrenadores/', busqueda_entrenador),
    path('buscar_jugadores/', busqueda_jugador),
    path('buscar_equipos/', busqueda_equipo),

]
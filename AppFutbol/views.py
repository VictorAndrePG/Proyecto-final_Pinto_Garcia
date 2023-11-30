from django.shortcuts import render, redirect
from AppFutbol.models import Equipo, Jugador, Entrenador
from AppFutbol.forms import EquipoForm, JugadorForm, EntrenadorForm, BusquedaFormJugador, BusquedaFormEntrenador, BusquedaFormEquipo

def mostrar_equipos(request):
    equipos = Equipo.objects.all()
    contexto = {"equipos": equipos, "form":BusquedaFormEquipo()}
    return render(request, 'equipos.html', contexto)

def agregar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_equipos')
    else:
        form = EquipoForm()

    return render(request, 'agregar_equipo.html', {'form': form})

def busqueda_equipo(request):
    nombre = request.GET.get("nombre", "")
    equipos = Equipo.objects.filter(nombre__icontains=nombre)
    contexto = {
        "equipos": equipos,
        "form": BusquedaFormEquipo(),
    }
    return render(request, "equipos.html", contexto)

def mostrar_jugadores(request):
    jugadores = Jugador.objects.all()
    contexto = {"jugadores": jugadores}
    return render(request, 'jugadores/jugadores.html', contexto)

def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_jugadores')
    else:
        form = JugadorForm()

    return render(request, 'jugadores/agregar_jugador.html', {'form': form})


def mostrar_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    contexto = {"entrenadores": entrenadores}
    return render(request, 'entrenador/entrenadores.html', contexto)

def agregar_entrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_entrenadores')
    else:
        form = EntrenadorForm()

    return render(request, 'entrenador/agregar_entrenador.html', {'form': form})

def seleccionar_categoria(request):
    return render(request, 'seleccionar_categoria.html')


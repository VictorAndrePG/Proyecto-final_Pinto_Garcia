from django import forms
from AppFutbol.models import Equipo, Jugador, Entrenador


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre']

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre']

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['nombre']

class BusquedaFormJugador(forms.Form):
    nombre = forms.CharField()

class BusquedaFormEquipo(forms.Form):
    nombre = forms.CharField()

class BusquedaFormEntrenador(forms.Form):
    nombre = forms.CharField()
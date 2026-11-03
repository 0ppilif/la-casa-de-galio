from django import forms
from .models import Figura3D, Reserva

class Figura3DForm(forms.ModelForm):
    class Meta:
        model = Figura3D
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'material': forms.Select(attrs={'class': 'form-select'}),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['figura', 'cantidad'] # Solo pedimos esto; el usuario y fecha se asignan solos
        widgets = {
            'figura': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }
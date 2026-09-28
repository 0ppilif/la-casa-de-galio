from django.shortcuts import render
from django.http import HttpResponse
# Importamos el modelo de la base de datos
from .models import Figura3D

# VISTA CATÁLOGO 3D
def inicio(request):
    # Consulta ORM: Obtenemos todas las figuras 3D
    impresiones = Figura3D.objects.all()
    data = {
        "catalogo_impresiones": impresiones
    }
    return render(request, 'bodega/inicio.html', data)

def usuario(request):
    data = {
        'nombre':'Armando',
        'apellidos':'Bronca Segura',
        'correo':'abronca@correo.cl',
        'cargo':'bodeguero'
    }
    return render(request,'bodega/usuario.html',data)
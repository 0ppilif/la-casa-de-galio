from django.shortcuts import render
from django.http import HttpResponse
# Importamos los modelos de la base de datos
from .models import Computador
from bodegaApp.models import Figura3D

# VISTA GLOBAL
def inicio_principal(request):
    # Consultas ORM: Obtenemos los primeros 2 registros de la BD
    preview_pcs = Computador.objects.all()[:2]
    preview_impresiones = Figura3D.objects.all()[:2]
    
    contexto = {
        'preview_pcs': preview_pcs, 
        'preview_impresiones': preview_impresiones
    }
    return render(request, 'tienda/home_principal.html', contexto)

# VISTA CATÁLOGO PC
def inicio(request):
    # Consulta ORM: Obtenemos todos los PCs
    pcs = Computador.objects.all()
    data = {
        "catalogo_pcs": pcs
    }
    return render(request, 'tienda/inicio.html', data)

def inventario(request):
    return HttpResponse("<h1>Mi inventario con Django</h1>")
from django.shortcuts import render
from django.http import HttpResponse
import json
import os
from django.conf import settings

# VISTA MODIFICADA: Catálogo completo de Impresiones 3D
def inicio(request):
    # 1. Definimos la ruta al archivo JSON de Impresiones 3D
    ruta_impresiones = os.path.join(settings.BASE_DIR, 'data', 'impresiones.json')
    
    # 2. Leemos el archivo JSON
    with open(ruta_impresiones, 'r', encoding='utf-8') as f:
        impresiones = json.load(f)
        
    # 3. Enviamos los datos al contexto con el nombre 'catalogo_impresiones'
    data = {
        "catalogo_impresiones": impresiones
    }
    
    return render(request, 'bodega/inicio.html', data)

# VISTA ORIGINAL: Se mantiene tu código de clases
def usuario(request):
    data = {
        'nombre':'Armando',
        'apellidos':'Bronca Segura',
        'correo':'abronca@correo.cl',
        'cargo':'bodeguero'
    }
    return render(request,'bodega/usuario.html',data)
from django.shortcuts import render
from django.http import HttpResponse
import json
import os
from django.conf import settings

# 1. NUEVA VISTA: Bienvenida Global y Vista Previa
def inicio_principal(request):
    # Definimos las rutas a los archivos JSON
    ruta_pcs = os.path.join(settings.BASE_DIR, 'data', 'pcs.json')
    ruta_impresiones = os.path.join(settings.BASE_DIR, 'data', 'impresiones.json')
    
    # Leemos los archivos
    with open(ruta_pcs, 'r', encoding='utf-8') as f:
        pcs = json.load(f)
        
    with open(ruta_impresiones, 'r', encoding='utf-8') as f:
        impresiones = json.load(f)
        
    # Pasamos los datos al contexto (solo los 2 primeros elementos para la vista previa)
    contexto = {
        'preview_pcs': pcs[:2], 
        'preview_impresiones': impresiones[:2]
    }
    
    return render(request, 'tienda/home_principal.html', contexto)


# 2. VISTA MODIFICADA: Catálogo completo de Los PC's de Galio
def inicio(request):
    # Ahora lee los datos reales desde el JSON en lugar de datos estáticos
    ruta_pcs = os.path.join(settings.BASE_DIR, 'data', 'pcs.json')
    
    with open(ruta_pcs, 'r', encoding='utf-8') as f:
        pcs = json.load(f)
        
    data = {
        "catalogo_pcs": pcs
    }
    return render(request, 'tienda/inicio.html', data)


# 3. VISTA INVENTARIO (Se mantiene tu código original de clases)
def inventario(request):
    return HttpResponse("<h1>Mi inventario con Django</h1>")
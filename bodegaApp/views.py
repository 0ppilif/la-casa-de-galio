from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Figura3D, Reserva
from .forms import Figura3DForm, ReservaForm

@login_required
def registrar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            # commit=False permite pausar el guardado para agregar datos manuales
            reserva = form.save(commit=False)
            reserva.usuario = request.user # Asignamos automáticamente al usuario logueado
            reserva.save() # Ahora sí lo guardamos definitivamente
            return redirect('dashboard') # Redirigimos al panel de control tras el éxito
    else:
        form = ReservaForm()
    
    return render(request, 'bodega/form_reserva.html', {'form': form, 'titulo': 'Registrar Reserva'})

@login_required
def listar_figuras(request):
    figuras = Figura3D.objects.all()
    return render(request, 'bodega/listar_figuras.html', {'figuras': figuras})

@login_required
def agregar_figura(request):
    if request.method == 'POST':
        form = Figura3DForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_figuras')
    else:
        form = Figura3DForm()
    return render(request, 'bodega/form_figura.html', {'form': form, 'titulo': 'Agregar Figura 3D'})

@login_required
def modificar_figura(request, id):
    figura = get_object_or_404(Figura3D, id=id)
    if request.method == 'POST':
        form = Figura3DForm(request.POST, request.FILES, instance=figura)
        if form.is_valid():
            form.save()
            return redirect('listar_figuras')
    else:
        form = Figura3DForm(instance=figura)
    return render(request, 'bodega/form_figura.html', {'form': form, 'titulo': 'Modificar Figura 3D'})

@login_required
def eliminar_figura(request, id):
    figura = get_object_or_404(Figura3D, id=id)
    figura.delete()
    return redirect('listar_figuras')

# VISTA CATÁLOGO 3D
def inicio(request):
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
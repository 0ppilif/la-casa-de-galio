from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Computador, Venta
from bodegaApp.models import Figura3D
from .forms import ComputadorForm, RegistroUsuarioForm, EditarUsuarioForm, VentaForm

@login_required
def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.vendedor = request.user 
            venta.save()
            
            if venta.computador:
                venta.computador.vendido = True
                venta.computador.save()
                
            if venta.figura:
                venta.figura.vendido = True
                venta.figura.save()
            
            # Redirección exacta al dashboard de mantenedores
            return redirect('dashboard') 
    else:
        form = VentaForm()
        
    return render(request, 'tienda/registrar_venta.html', {'form': form})

@login_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    es_admin = request.user.username == 'ola'
    return render(request, 'tienda/listar_usuarios.html', {'usuarios': usuarios, 'es_admin': es_admin})

@login_required
def agregar_usuario(request):
    if request.user.username != 'ola':
        return redirect('listar_usuarios')

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'tienda/form_usuario.html', {'form': form, 'titulo': 'Agregar Usuario'})

@login_required
def modificar_usuario(request, id):
    if request.user.username != 'ola':
        return redirect('listar_usuarios')
        
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = EditarUsuarioForm(instance=usuario)
    return render(request, 'tienda/form_usuario.html', {'form': form, 'titulo': 'Modificar Usuario'})

@login_required
def eliminar_usuario(request, id):
    if request.user.username != 'ola':
        return redirect('listar_usuarios')

    usuario = get_object_or_404(User, id=id)
    
    # Bloqueo para proteger la cuenta admin y correo personal
    if usuario.username == 'ola' or usuario.email == 'filippomoreno.128@gmail.com':
        return redirect('listar_usuarios')
        
    usuario.delete()
    return redirect('listar_usuarios')

@login_required
def listar_pcs(request):
    computadores = Computador.objects.all()
    return render(request, 'tienda/listar_pcs.html', {'computadores': computadores})

@login_required
def agregar_pc(request):
    if request.method == 'POST':
        form = ComputadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_pcs')
    else:
        form = ComputadorForm()
    return render(request, 'tienda/form_pc.html', {'form': form, 'titulo': 'Agregar Computador'})

@login_required
def modificar_pc(request, id):
    pc = get_object_or_404(Computador, id=id)
    if request.method == 'POST':
        form = ComputadorForm(request.POST, request.FILES, instance=pc)
        if form.is_valid():
            form.save()
            return redirect('listar_pcs')
    else:
        form = ComputadorForm(instance=pc)
    return render(request, 'tienda/form_pc.html', {'form': form, 'titulo': 'Modificar Computador'})

@login_required
def eliminar_pc(request, id):
    pc = get_object_or_404(Computador, id=id)
    pc.delete()
    return redirect('listar_pcs')

@login_required
def dashboard(request):
    es_admin = request.user.groups.filter(name='Administrador').exists() or request.user.username == 'ola'
    es_supervisor = request.user.groups.filter(name='Supervisor').exists()
    es_administrativo = request.user.groups.filter(name='Administrativo').exists()
    
    if request.user.is_superuser:
        es_admin = True

    context = {
        'es_admin': es_admin,
        'es_supervisor': es_supervisor,
        'es_administrativo': es_administrativo,
    }
    return render(request, 'tienda/dashboard.html', context)

def inicio_principal(request):
    preview_pcs = Computador.objects.all()[:2]
    preview_impresiones = Figura3D.objects.all()[:2]
    
    contexto = {
        'preview_pcs': preview_pcs, 
        'preview_impresiones': preview_impresiones
    }
    return render(request, 'tienda/home_principal.html', contexto)

def inicio(request):
    pcs = Computador.objects.all()
    data = {
        "catalogo_pcs": pcs
    }
    return render(request, 'tienda/inicio.html', data)

def inventario(request):
    return HttpResponse("<h1>Mi inventario con Django</h1>")
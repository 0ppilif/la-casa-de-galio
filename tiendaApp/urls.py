from django.contrib import admin
from django.urls import path
# importar la vista desde la App
from tiendaApp import views as vistita
from . import views

urlpatterns = [
    # path(lo_que_escribe_el_usuario , funcion_que_carga_la_vista)
    path('inventario/',vistita.inventario, name="inventario"),
    path('',vistita.inicio,name="home_tienda"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('mantenedor/pcs/', views.listar_pcs, name='listar_pcs'),
    path('mantenedor/pcs/agregar/', views.agregar_pc, name='agregar_pc'),
    path('mantenedor/pcs/modificar/<int:id>/', views.modificar_pc, name='modificar_pc'),
    path('mantenedor/pcs/eliminar/<int:id>/', views.eliminar_pc, name='eliminar_pc'),
    path('mantenedor/usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('mantenedor/usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('mantenedor/usuarios/modificar/<int:id>/', views.modificar_usuario, name='modificar_usuario'),
    path('mantenedor/usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('transaccion/venta/', views.registrar_venta, name='registrar_venta'),
]

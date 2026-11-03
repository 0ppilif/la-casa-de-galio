from django.contrib import admin
from django.urls import path
# importar la vista desde la App
from bodegaApp import views
from . import views

urlpatterns = [
    path('',views.inicio,name="home_bodega"),
    # (lo_que_el_usuario_escribe, vista_que_debo_cargar, nombre_para_llamar_desde_template)
    path('user/',views.usuario,name="user"),
    path('mantenedor/figuras/', views.listar_figuras, name='listar_figuras'),
    path('mantenedor/figuras/agregar/', views.agregar_figura, name='agregar_figura'),
    path('mantenedor/figuras/modificar/<int:id>/', views.modificar_figura, name='modificar_figura'),
    path('mantenedor/figuras/eliminar/<int:id>/', views.eliminar_figura, name='eliminar_figura'),
    path('transaccion/reserva/', views.registrar_reserva, name='registrar_reserva')
]

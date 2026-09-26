from django.contrib import admin
from django.urls import path
# importar la vista desde la App
from bodegaApp import views

urlpatterns = [
    path('',views.inicio,name="home_bodega"),
    # (lo_que_el_usuario_escribe, vista_que_debo_cargar, nombre_para_llamar_desde_template)
    path('user/',views.usuario,name="user")
]

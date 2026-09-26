from django.contrib import admin
from django.urls import path
# importar la vista desde la App
from tiendaApp import views as vistita

urlpatterns = [
    # path(lo_que_escribe_el_usuario , funcion_que_carga_la_vista)
    path('inventario/',vistita.inventario, name="inventario"),
    path('',vistita.inicio,name="home_tienda")
]

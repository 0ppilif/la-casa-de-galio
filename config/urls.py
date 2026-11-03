from django.contrib import admin
from django.urls import path,include
# importar la vista desde la App
from tiendaApp import views as tienda_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path(lo_que_escribe_el_usuario , funcion_que_carga_la_vista)
    path('tienda/',include('tiendaApp.urls')),
    path('bodega/',include('bodegaApp.urls')),
path('', tienda_views.inicio_principal, name="inicio_global"),
    #****************/app/ruta dentro app
    # 127.0.0.1:8000/tienda/inventario/
    
]

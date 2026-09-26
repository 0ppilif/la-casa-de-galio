from django.contrib import admin
from .models import Categoria, Computador

# Registramos las tablas para que aparezcan en el panel de administración
admin.site.register(Categoria)
admin.site.register(Computador)
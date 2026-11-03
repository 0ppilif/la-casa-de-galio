from django.db import models
from django.contrib.auth.models import User
from bodegaApp.models import Figura3D

# Tabla 1: Categoría del PC (Ej: Gamer, Oficina, Workstation)
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de Categoría")

    def __str__(self):
        return self.nombre

# Tabla 2: Computadores
class Computador(models.Model):
    nombre = models.CharField(max_length=100)
    # Llave foránea que relaciona el PC con una Categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="computadores")
    procesador = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)
    gpu = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tarjeta Gráfica")
    monitor = models.CharField(max_length=100, blank=True, null=True)
    perifericos = models.CharField(max_length=200, blank=True, null=True)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.CharField(max_length=200, help_text="Ejemplo: images/pc1.jpeg")
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    computador = models.ForeignKey(Computador, on_delete=models.CASCADE, null=True, blank=True)
    figura = models.ForeignKey(Figura3D, on_delete=models.CASCADE, null=True, blank=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Venta {self.id} por {self.vendedor}"
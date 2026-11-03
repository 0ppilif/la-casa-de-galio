from django.db import models
from django.contrib.auth.models import User

# Tabla 1: Material de impresión (Ej: Resina, PLA, ABS)
class Material(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Tabla 2: Figuras 3D
class Figura3D(models.Model):
    nombre = models.CharField(max_length=100)
    # Llave foránea que relaciona la figura con un Material
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="figuras")
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.CharField(max_length=200, help_text="Ejemplo: images/impresion1.jpeg")
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    figura = models.ForeignKey(Figura3D, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return f"Reserva de {self.usuario.username} - {self.figura.nombre}"
from django.db import models

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

    def __str__(self):
        return self.nombre
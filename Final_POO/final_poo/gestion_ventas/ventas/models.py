from django.db import models


class ventas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

# Create your models here.
# ventas/models.py
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class ProductoTecnologico(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    producto = models.ForeignKey(ProductoTecnologico, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.producto.precio
        if self.producto.stock < self.cantidad:
            raise ValueError("No hay suficiente stock para completar la venta")
        self.producto.stock -= self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta de {self.producto.nombre} - {self.cantidad} unidades"

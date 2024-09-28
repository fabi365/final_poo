from django.contrib import admin

# Register your models here.
# ventas/admin.py
from django.contrib import admin
from .models import Cliente, ProductoTecnologico, Venta

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'direccion')

@admin.register(ProductoTecnologico)
class ProductoTecnologicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'stock')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'cantidad', 'fecha', 'total')


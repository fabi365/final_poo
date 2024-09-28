# ventas/forms.py
from django import forms
from .models import ProductoTecnologico, Venta, Cliente


class ProductoTecnologicoForm(forms.ModelForm):
    class Meta:
        model = ProductoTecnologico
        fields = ['nombre', 'descripcion', 'precio', 'stock']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto', 'cantidad', 'fecha']

# ventas/forms.py

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion']

class ProductoTecnologicoForm(forms.ModelForm):
    class Meta:
        model = ProductoTecnologico
        fields = ['nombre', 'descripcion', 'precio', 'stock']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'cantidad', 'fecha']


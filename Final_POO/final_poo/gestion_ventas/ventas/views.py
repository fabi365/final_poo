from django.shortcuts import render, redirect
from .forms import ProductoTecnologicoForm, VentaForm
from .models import ProductoTecnologico, Venta
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, ProductoTecnologicoForm, VentaForm
from .models import Cliente, ProductoTecnologico, Venta

def home(request):
    return render(request, 'ventas/home.html')


def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoTecnologicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoTecnologicoForm()
    return render(request, 'ventas/registrar_producto.html', {'form': form})

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'ventas/registrar_venta.html', {'form': form})

def lista_productos(request):
    productos = ProductoTecnologico.objects.all()
    return render(request, 'ventas/lista_productos.html', {'productos': productos})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})

# Vistas para Clientes
def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'ventas/registrar_cliente.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/lista_clientes.html', {'clientes': clientes})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'ventas/editar_cliente.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'ventas/eliminar_cliente.html', {'cliente': cliente})

# Vistas para Productos
def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoTecnologicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoTecnologicoForm()
    return render(request, 'ventas/registrar_producto.html', {'form': form})

def lista_productos(request):
    productos = ProductoTecnologico.objects.all()
    return render(request, 'ventas/lista_productos.html', {'productos': productos})

def editar_producto(request, pk):
    producto = get_object_or_404(ProductoTecnologico, pk=pk)
    if request.method == 'POST':
        form = ProductoTecnologicoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoTecnologicoForm(instance=producto)
    return render(request, 'ventas/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(ProductoTecnologico, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'ventas/eliminar_producto.html', {'producto': producto})

# Vistas para Ventas
def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'ventas/registrar_venta.html', {'form': form})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})


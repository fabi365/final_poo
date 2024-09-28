# ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar-producto/', views.registrar_producto, name='registrar_producto'),
    path('registrar-venta/', views.registrar_venta, name='registrar_venta'),
    path('lista-productos/', views.lista_productos, name='lista_productos'),
    path('lista-ventas/', views.lista_ventas, name='lista_ventas'),
    path('registrar-cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('lista-clientes/', views.lista_clientes, name='lista_clientes'),
    path('editar-cliente/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar-cliente/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('registrar-producto/', views.registrar_producto, name='registrar_producto'),
    path('lista-productos/', views.lista_productos, name='lista_productos'),
    path('editar-producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar-producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('registrar-venta/', views.registrar_venta, name='registrar_venta'),
    path('lista-ventas/', views.lista_ventas, name='lista_ventas'),
]

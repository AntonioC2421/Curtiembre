from django.urls import path
from .Views.Producto.productos import All_Product
from .Views.Ingreso_Producto.ingreso_producto import Add_Product

urlpatterns = [
  path('All-Product/', All_Product, name='Producto'),
  path('Add-Product/', Add_Product, name='IngresoProducto'),
  
]

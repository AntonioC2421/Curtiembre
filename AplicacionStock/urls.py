from django.urls import path
from .Views.Producto.productos import All_Product
from .Views.Ingreso_Producto.ingreso_producto import Add_Product
from .Views.Cuero.cuero import Cuero
from .Views.Venta.venta import Resgistro_Venta
from .Views.Consumo.consumo import Consumo
from .Views.Otros.clientes import Otros_Cliente
from .Views.Otros.manuales import Otros_Manuales
from .Views.Otros.proveedores import Otros_Proveedores

urlpatterns = [
  path('All-Product/', All_Product, name='Producto'),
  path('Add-Product/', Add_Product, name='IngresoProducto'),
  path('Cuero/', Cuero, name='Cuero'),
  path('Registro-Venta/', Resgistro_Venta, name='ResgistroVenta'),
  path('Consumo/', Consumo, name='Consumo'),
  path('Otros-clientes', Otros_Cliente, name='MainOtros'),
  path('Otros-proveedores', Otros_Proveedores, name='OtrosProveedores'),
  path('Otros-manuales', Otros_Manuales, name='OtrosManuales')
]
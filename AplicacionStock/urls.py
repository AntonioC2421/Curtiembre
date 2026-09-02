from django.urls import path
from .Views.Producto.productos import All_Product

urlpatterns = [
  path('All-Product/', All_Product)
]

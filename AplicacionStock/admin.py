from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Sede)
admin.site.register(TipoCuero)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(ProductoSede)
admin.site.register(Consumo)
admin.site.register(Cuero)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

class Sede(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class TipoCuero(models.Model):
    nombre = models.CharField(max_length=25)

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=25)

class Producto(models.Model):
    imagen = models.ImageField(upload_to='static/img/img_producto', blank=True, null=True)
    nombre = models.CharField(max_length=50)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    tipo_producto= models.ForeignKey(TipoProducto, on_delete=models.PROTECT)

class ProductoSede(models.Model):
    stock_sede = models.PositiveIntegerField(default=0)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT)

    # Evitar duplicar el mismo producto en la misma sede
    class Meta:
        unique_together = ('producto', 'sede')

class Consumo(models.Model):
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    producto_sede = models.ForeignKey(ProductoSede, on_delete=models.PROTECT)

class Cuero(models.Model):
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('VENDIDO', 'Vendido'),
    ]

    espesor = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0.01)], help_text="Espesor en mm")
    area = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='DISPONIBLE')
    codigo_color = models.CharField(max_length=30)
    nombre_color = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoCuero, on_delete=models.PROTECT, related_name='cueros')
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT, related_name='cueros')

class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    precio_total = models.DecimalField(max_digits=6, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

class DetalleVenta(models.Model):
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    cuero = models.ForeignKey(Cuero, on_delete=models.PROTECT)

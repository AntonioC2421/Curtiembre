from django import forms
from AplicacionStock.models import ProductoSede, Proveedor, TipoProducto, Sede

class RegistrarProductoSedeForm(forms.ModelForm):
    # Campos adicionales para asociar imágenes y Producto
    imagen = forms.ImageField(required=False)
    nombre_producto = forms.CharField(max_length=50, label="Nombre del producto")
    
    # Se obtienen solo las instancias preexistentes
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        label="Proveedor",
        empty_label="Seleccione un proveedor"
    )
    tipo_producto = forms.ModelChoiceField(
        queryset=TipoProducto.objects.all(),
        label="Tipo de Producto",
        empty_label="Seleccione un tipo de producto"
    )

    class Meta:
        model = ProductoSede
        fields = ['stock_sede', 'sede']
        labels = {
            'stock_sede': 'Cantidad',
            'sede': 'Sede',
        }
        widgets = {
            'sede': forms.RadioSelect(),
        }
from django.shortcuts import render, redirect
from AplicacionStock.Views.View_Quantity import get_quantity_objects
from AplicacionStock.forms import RegistrarProductoSedeForm
from django.contrib import messages
from AplicacionStock.models import Producto, Proveedor, TipoProducto, ProductoSede

def Add_Product(request):
    if request.method == 'POST':
        form_producto_sede = RegistrarProductoSedeForm(request.POST, request.FILES)
        
        if form_producto_sede.is_valid():
            # Obtener los datos COMPLETOS ya registrados 
            nombre_prod = form_producto_sede.cleaned_data['nombre_producto']
            proveedor_obj = form_producto_sede.cleaned_data['proveedor'] # Ya es una instancia de Proveedor
            tipo_prod_obj = form_producto_sede.cleaned_data['tipo_producto'] # Ya es una instancia de TipoProducto
            imagen_prod = form_producto_sede.cleaned_data.get('imagen')
            
            stock_sede = form_producto_sede.cleaned_data['stock_sede']
            sede_obj = form_producto_sede.cleaned_data['sede']

            # Buscar si el Producto existe o crearlo si es completamente nuevo
            producto_obj, _ = Producto.objects.get_or_create(
                nombre=nombre_prod,
                proveedor=proveedor_obj,
                tipo_producto=tipo_prod_obj,
                defaults={'imagen': imagen_prod}
            )

            # Guardar o actualizar ProductoSede
            obj_producto_sede, created = ProductoSede.objects.get_or_create(
                producto=producto_obj,
                sede=sede_obj,
                defaults={'stock_sede': stock_sede}
            )

            if not created:
                obj_producto_sede.stock_sede += stock_sede
                obj_producto_sede.save()

            messages.success(request, "Producto ingresado correctamente")
            return redirect('IngresoProducto')
        else:
            messages.error(request, "Error al ingresar el producto. Revisa los datos.")
    else:
        form_producto_sede = RegistrarProductoSedeForm()

    quantity = get_quantity_objects('ProductoSede', 5)
    proveedores = Proveedor.objects.all()
    tipos_producto = TipoProducto.objects.all()
    data = {
        'Form_Producto_Sede': form_producto_sede,
        'proveedores': proveedores,
        'tipos_producto': tipos_producto,
    }

    return render(
        request,
        'template_aplicacion/ingreso_producto.html',
        {'data_quantity': quantity, 'data': data},
    )
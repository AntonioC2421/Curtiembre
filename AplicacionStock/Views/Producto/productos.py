from django.shortcuts import render
from AplicacionStock.Views.View_All import get_all_objects

def All_Product(request):
    Name_Model = 'ProductoSede' 
    All_Product = get_all_objects(Name_Model)
    return render(request, 'template_aplicacion/productos.html', {'data_all': All_Product})

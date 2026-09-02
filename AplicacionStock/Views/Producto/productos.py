from django.shortcuts import render

def All_Product (request):
    return render(request, 'template_aplicacion/productos.html')
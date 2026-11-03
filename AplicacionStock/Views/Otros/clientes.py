from django.shortcuts import render

def Otros_Cliente(request):
    return render(request, 'template_aplicacion/template_otros/otros_cliente.html')
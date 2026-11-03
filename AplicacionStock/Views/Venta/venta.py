from django.shortcuts import render

def Resgistro_Venta(request):
    return render(request, 'template_aplicacion/RegistroVenta.html')
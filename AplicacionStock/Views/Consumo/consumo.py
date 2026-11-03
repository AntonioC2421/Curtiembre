from django.shortcuts import render

def Consumo(request):
    return render(request, 'template_aplicacion/consumo.html')
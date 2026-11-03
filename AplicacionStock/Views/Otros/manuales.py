from django.shortcuts import render

def Otros_Manuales(request):
    return render(request, 'template_aplicacion/template_otros/otros_manual.html')
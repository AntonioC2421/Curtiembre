from django.shortcuts import render
from AplicacionStock.models import Cuero, Sede, TipoCuero

def Cuero(request):
    sede = Sede.objects.all()
    tipos_cuero = TipoCuero.objects.all()
    data = {
        'sede':sede,
        'tipos_cuero':tipos_cuero
    }
    return render(request, 'template_aplicacion/template_cuero/cuero_venta.html', {'data':data})
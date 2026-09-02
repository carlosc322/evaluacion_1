from django.shortcuts import render
from NexoDigitalSoluciones.models import mostrarInformacion
# Create your views here.

def mostrarInicio(request):

    return render(request,'index.html')

def mostrarServicio(request):
    return render(request, 'servicio.html')

def mostrarContacto(request):
    return render(request, 'contacto.html')


def mostrarNosotros(request):
    return render(request,'nosotros.html')



def mostrarBase(request):
    return render(request, 'base.html')

def servAplicaciones(request):
    context = mostrarInformacion()
    return render(request,'servAplicaciones.html', context)

def servCiberseguridad(request):
    context = mostrarInformacion()
    return render(request,'servCiberseguridad.html', context)

def servConsultoria(request):
    context = mostrarInformacion()
    return render(request, 'servConsultoria.html', context)

def servDesarrollo(request):
    context = mostrarInformacion()
    return render(request,'servDesarrollo.html', context)

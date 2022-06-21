from django.shortcuts import render
from .models import Post


def home(request):
    data = Post.objects.all()
    return render(request, 'network/home.html', {'posts': data})


def agregarAporte(request):
    return render(request, 'network/agregar_aporte.html')

def agregarAnotacion(request):
    return render(request, 'network/agregaranotacion.html')

def anotaciones(request):
    return render(request, 'network/anotaciones.html')

def aportes(request):
    return render(request, 'network/aportes.html')

def controlResidentes(request):
    return render(request, 'network/Control_de_residentes.html')

def fichapaciente(request):
    return render(request, 'network/ficha_paciente.html')

def informacion(request):
    return render(request, 'network/informacion.html')

def ingresos(request):
    return render(request, 'network/ingresos.html')

def insumos(request):
    return render(request, 'network/insumos.html')

def residentesAfuera(request):
    return render(request, 'network/residentes_fuera.html')

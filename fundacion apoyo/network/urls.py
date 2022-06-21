from django.urls import path
from . import views


app_name = 'network'

urlpatterns = [
    path('', views.home, name='home'),
    path('agregarAporte', views.agregarAporte, name='agregarAporte'),
    path('agregarAnotacion', views.agregarAnotacion, name='agregarAnotacion'),
    path('anotaciones', views.anotaciones, name='anotaciones'),
    path('aportes', views.aportes, name='aportes'),
    path('controlResidentes', views.controlResidentes, name='controlResidentes'),
    path('fichapaciente', views.fichapaciente, name='fichapaciente'),
    path('informacion', views.informacion, name='informacion'),
    path('ingresos', views.ingresos, name='ingresos'),
    path('insumos', views.insumos, name='insumos'),
    path('residentesAfuera', views.residentesAfuera, name='residentesAfuera'),
]
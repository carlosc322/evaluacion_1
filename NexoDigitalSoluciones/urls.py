from django.contrib import admin
from django.urls import path, include
from NexoDigitalSoluciones import views


urlpatterns = [
    path('mostrarBase/', views.mostrarBase, name= 'mostrarBase'),
    path('',views.mostrarInicio, name='mostrarInicio'),
    path('mostrarServicio/', views.mostrarServicio, name='mostrarServicio'),
    path('mostrarContacto/', views.mostrarContacto, name='mostrarContacto'),
    path('mostrarNosotros/', views.mostrarNosotros, name='mostrarNosotros'),

    path('servicioAplicaciones/', views.servAplicaciones, name='servAplicaciones'),
    path('servicioCiberseguridad/',views.servCiberseguridad, name='servCiberseguridad'),
    path('servicioConsultoria/', views.servConsultoria, name='servConsultoria'),
    path('servicioDesarrollo/', views.servDesarrollo, name='servDesarrollo')


]
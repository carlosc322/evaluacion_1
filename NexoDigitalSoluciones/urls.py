from django.contrib import admin
from django.urls import path, include
from NexoDigitalSoluciones import views


urlpatterns = [
    path('',views.mostrarInicio, name='mostrarInicio'),
    path('mostrarServicio/', views.mostrarServicio, name='mostrarServicio')
    
]
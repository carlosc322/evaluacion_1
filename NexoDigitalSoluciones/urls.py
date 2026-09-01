from django.contrib import admin
from django.urls import path, include
from NexoDigitalSoluciones import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mostrarInicio)
    
]
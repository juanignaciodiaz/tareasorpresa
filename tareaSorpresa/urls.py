from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('agregar/', views.agregarNota, name='agregarNota'),
    path('eliminar/<int:idNota>', views.eliminarNota, name='eliminarNota'),
]

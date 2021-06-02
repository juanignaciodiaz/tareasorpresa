from django.db import models
from django import forms
# Create your models here.

class Nota(models.Model):

    titulo = models.CharField('Titulo nota:', max_length=50, blank=False, null=False)
    descripcion = models.TextField('Descripcion:')
    fecha_creacion = models.DateTimeField('Fecha creacion:', auto_now_add=True)
    fecha_finalizacion = models.DateField('Fecha finalizacion:')
    estado = models.BooleanField('Estado:', default= 0)


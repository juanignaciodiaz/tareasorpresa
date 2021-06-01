from django.db import models

# Create your models here.

class Nota(models.Model):

    titulo = models.CharField('Titulo nota:', max_length=50, blank=False, null=False)
    descripcion = models.CharField('Descripcion:', max_length=150, blank=False, null=False)
    fecha_creacion = models.DateTimeField('Fecha creacion:', auto_now_add=True)
    fecha_finalizacion = models.DateTimeField('Fecha finalizacion:', auto_now=True)
    estado = models.CharField('Estado:', max_length=30, blank=True, null=True)


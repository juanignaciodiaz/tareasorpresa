from django.shortcuts import redirect, render
from .models import Nota
from .forms import FormularioNota
from datetime import datetime

# Create your views here.

def principal(request):
    
    notas = Nota.objects.all()
    context = {
        'notas': notas
    }

    for nota in notas:
        if validarFecha(nota.fecha_finalizacion):
            nota.estado = 0
        else:
            nota.estado = 1

    return render(request, 'pages/principal.html', context)


def agregarNota(request):
    
    formulario = FormularioNota()

    if request.method == 'POST':
        formulario = FormularioNota(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('principal')


    context = {
        'formulario': formulario
    }
    return render(request, 'pages/agregar.html', context) 

def validarFecha(fecha1):
    fecha_hoy = datetime.today().strftime('%Y-%m-%d')
    validacion = False
    fecha_str = str(fecha1)

    if fecha_str < fecha_hoy:
        validacion = True

    return validacion

def eliminarNota(request, idNota):
    notaEncontrada = None
    try:
        notaEncontrada = Nota.objects.get(pk = idNota)
        notaEncontrada.delete()
    except:
        pass
    return redirect('principal')
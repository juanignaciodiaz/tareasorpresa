from django.shortcuts import render
from .models import Nota
from .forms import FormularioNota

# Create your views here.

def principal(request):
    notas = Nota.objects.all()
    context = {
        'notas': notas
    }

    return render(request, 'pages/principal.html', context)
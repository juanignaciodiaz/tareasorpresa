from django import forms
from .models import Nota

class FormularioNota(forms.ModelForm):
    class Meta:
        Model = Nota
        fields = "__all__"
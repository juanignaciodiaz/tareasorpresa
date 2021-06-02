from django import forms
from .models import Nota

class FormularioNota(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormularioNota, self).__init__(*args, **kwargs)
        for campovisible in self.visible_fields():
            campovisible.field.widget.attrs['class'] = 'form-control'
            

    class Meta:
        model = Nota
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows':4, 'cols':15}),
            'fecha_finalizacion': forms.DateTimeInput(attrs={'type': 'date'}),
            'estado': forms.CheckboxInput(attrs={'disabled': 'true'}),
        }
        fields = '__all__'
from django import forms
from .models import Empleados, Cargo


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['nombre', 'apellido_materno',
                  'apellido_paterno', 'doc_identidad', 'correo', 'telefono', 'cargo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cargo'].queryset = Cargo.objects.all()

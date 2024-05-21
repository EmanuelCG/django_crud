from django import forms
from .models import Empleados


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['nombre', 'apellido_materno',
                  'apellido_paterno', 'doc_identidad', 'correo', 'telefono']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cargo'].queryset = Cargo.objects.all()
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = "form-control"

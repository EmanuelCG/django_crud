from django import forms
from .models import Empleados
from .models import Cargo
from .models import Area


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['nombre', 'apellido_materno',
                  'apellido_paterno', 'doc_identidad', 'correo', 'telefono', 'area', 'cargo', 'image_profile']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cargo'].queryset = Cargo.objects.all()
        self.fields['area'].queryset = Area.objects.all()
        for field_name, field in self.fields.items():
            if field_name == 'cargo' or field_name == 'area':
                field.widget.attrs['class'] = "form-select"
            else:
                field.widget.attrs['class'] = "form-control"

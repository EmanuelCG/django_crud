from django.contrib import admin
from .models import Empleados
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno',
                    'apellido_materno', 'correo', 'telefono')
    list_display_links = ('nombre', 'apellido_paterno',
                          'apellido_materno')


admin.site.register(Empleados, EmpleadoAdmin)

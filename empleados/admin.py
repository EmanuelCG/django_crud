from django.contrib import admin
from .models import Empleados, Cargo
# Register your models here.


class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'area')


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno',
                    'apellido_materno', 'correo', 'telefono', 'cargo')
    list_display_links = ('nombre', 'apellido_paterno',
                          'apellido_materno')


admin.site.register(Empleados, EmpleadoAdmin)
admin.site.register(Cargo, CargoAdmin)

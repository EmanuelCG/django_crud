from django.contrib import admin
from .models import Area


class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

    # def mostrar_puestos(self, obj):
    #     return ", ".join([cargo.nombre for cargo in obj.cargo.all()])
    # mostrar_puestos.short_description = "Puestos"


admin.site.register(Area, AreaAdmin)

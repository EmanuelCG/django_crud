from django.db import models
from area.models import Area
from cargo.models import Cargo
# Create your models here.


class Empleados(models.Model):
    nombre = models.CharField(max_length=250, blank=False)
    apellido_paterno = models.CharField(max_length=100, blank=False)
    apellido_materno = models.CharField(max_length=100, blank=False)
    doc_identidad = models.CharField(max_length=12, null=False)
    correo = models.EmailField(max_length=250)
    telefono = models.CharField(max_length=20, blank=False)
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, null=True, blank=True)
    cargo = models.ForeignKey(
        Cargo, on_delete=models.CASCADE, null=True, blank=True)
    image_profile = models.ImageField(
        upload_to='photos/profile', null=True, blank=True)
    estado = models.BooleanField(default=True)
    f_inicio = models.DateField(null=True, blank=True)
    f_cese = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "empleados"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return self.nombre

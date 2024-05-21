from django.db import models

# Create your models here.


class Cargo(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "cargo"

    def __str__(self):
        return f"{self.nombre} | {self.area}"


class Empleados(models.Model):
    nombre = models.CharField(max_length=250, blank=False)
    apellido_paterno = models.CharField(max_length=100, blank=False)
    apellido_materno = models.CharField(max_length=100, blank=False)
    doc_identidad = models.CharField(max_length=12, null=False)
    correo = models.EmailField(max_length=250)
    telefono = models.CharField(max_length=20, blank=False)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, blank=False)
    image_profile = models.ImageField(
        upload_to='photos/profile', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    f_ingreso = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "empleados"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return self.nombre

from django.db import models

# Create your models here.


class Personal(models.Model):
    nombre = models.CharField(max_length=250, blank=False)
    apellido_materno = models.CharField(max_length=100, blank=False)
    apellido_paterno = models.CharField(max_length=100, blank=False)
    correo = models.EmailField(max_length=250)
    telefono = models.CharField(max_length=20, blank=False)
    cargo = models.CharField(max_length=250, blank=False)
    image_profile = models.ImageField(
        upload_to='photos/profile', null=True, blank=True)
    is_active = models.BooleanField(default=True)

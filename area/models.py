from django.db import models
from cargo.models import Cargo
# Create your models here.


class Area(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    cargo = models.ManyToManyField(Cargo)
    descripcion = models.TextField(null=True)

    class Meta:
        db_table = "area"

    def __str__(self):
        return self.nombre

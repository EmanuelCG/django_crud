from django.db import models

# Create your models here.


class Cargo(models.Model):
    nombre = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "cargo"

    def __str__(self):
        return self.nombre

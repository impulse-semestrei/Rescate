from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

######## MODEL US36 ########
#### MODEL US21 ####


class Material(models.Model):
    codigo = models.CharField(max_length=100, unique=True, null=True)
    nombre = models.CharField(max_length=100, unique=True, null=False)
    descripcion = models.TextField(null=False)
    cantidad = models.IntegerField(null=False, validators=[MaxValueValidator(10000), MinValueValidator(0)])
    status = models.BooleanField(default=True, null=False)
    fecha_mod = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.nombre


#### MODEL US21 ####
######## MODEL US36 ########

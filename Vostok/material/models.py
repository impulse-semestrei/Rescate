from django.db import models
from django.utils import timezone

######## MODEL US36 ########

class Material(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False)
    descripcion = models.TextField(null=False)
    status = models.BooleanField(default=True, null=False)
    fechaMod = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.nombre

######## MODEL US36 ########




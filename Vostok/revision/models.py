from django.db import models
from inventario.models import Inventario
from django.utils import timezone


######## MODEL US41 ########


class Revision(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=False, default=timezone.now())
######## MODEL US41 ########

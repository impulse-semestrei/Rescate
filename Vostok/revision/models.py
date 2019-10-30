from django.db import models
from inventario.models import Inventario
from django.utils import timezone


######## MODEL US41 ########


class Revision(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    nombre_paramedico = models.CharField(max_length=100, null=False)
    email_paramedico = models.CharField(max_length=100, null=False)
    fecha = models.DateTimeField(null=False, default=timezone.now)
######## MODEL US41 ########



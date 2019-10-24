from django.db import models
from inventario.models import Inventario
from django.utils import timezone

####### MODELS US44############
class Ambulancia(models.Model):
    nombre = models.CharField(max_length=255, null=False, unique=True)
    status = models.BooleanField(default=True)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, unique=True)
    fecha_mod = models.DateField(null=False, default=timezone.now())
####### MODELS US44############

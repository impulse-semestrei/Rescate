from django.db import models
from inventario.models import Inventario

####### MODELS US44############
class Ambulancia(models.Model):
    nombre = models.CharField(max_length=255,null=False, unique=True)
    status = models.BooleanField(default=True)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, unique=True)
####### MODELS US44############

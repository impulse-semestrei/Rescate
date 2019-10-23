from django.db import models
from material.models import Material
from django.utils import timezone


######## MODEL US04########
####### MODEL US03 ########
class Inventario(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False)
    materiales = models.ManyToManyField(Material,through='InventarioMaterial')
    status = models.BooleanField(default=True,null=False)
    fechaMod=models.DateTimeField(default=timezone.now,null=False)

####### MODEL US03 ########
####### MODELS US-04############


######## MODELS US1 ########


class InventarioMaterial(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    fecha = models.DateTimeField(null=False,default=timezone.now)


######## MODELS US1 ########

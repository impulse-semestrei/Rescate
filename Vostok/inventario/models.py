from django.db import models
from material.models import Material
from django.utils import timezone


######## MODEL US04########
####### MODEL US03 ########
class Inventario(models.Model):  #crea el modelo para inventario en la base de datos#
    nombre = models.CharField(max_length=100, unique=True, null=False)
    # Solo puede haber un nombre de cada modelo solo puede haber un material, por lo que debe ser único
    # Además de que no se puede dejar vacio
    materiales = models.ManyToManyField(Material,through='InventarioMaterial')
    #Pone en lista Materiales creados para que los puedas añadir al inventario que estás creando.
    status = models.BooleanField(default=True, null=False)
    fechaMod = models.DateTimeField(default=timezone.now, null=False)
####### MODEL US03 ########
####### MODELS US-04############


######## MODELS US1 ########


class InventarioMaterial(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)


######## MODELS US1 ########

from django.db import models
from material.models import Material
from django.utils import timezone

######## MODEL US04########
####### MODEL US03 ########
class Inventario(models.Model):  #crea el modelo para inventario en la base de datos#
    nombre = models.CharField(max_length=100,unique=True,null=False)
    materiales = models.ManyToManyField(Material,through='Inventario_Material')
    status = models.BooleanField(default=True,null=False)
    fechaMod=models.DateTimeField(default=timezone.now,null=False)
####### MODEL US03 ########



class Inventario_Material(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
####### MODEL US04###########



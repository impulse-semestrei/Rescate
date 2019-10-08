from django.db import models
from material.models import Material

####### MODELS US-04############
class Inventario(models.Model):  #crea el modelo para inventario en la base de datos#
    nombre = models.CharField(max_length=100,unique=True,null=False)
    #Solo puede haber un nombre de cada modelo solo puede haber un material, por lo que debe ser único
    #Además de que no se puede dejar vacio
    materiales = models.ManyToManyField(Material,through='InventarioMaterial')
    #Pone en lista Materiales creados para que los puedas añadir al inventario que estás creando.


class InventarioMaterial(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
####### MODELS US-04############



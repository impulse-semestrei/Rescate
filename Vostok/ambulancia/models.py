from django.db import models
from inventario.models import Inventario
from django.utils import timezone
from revision.models import Revision
from django.core.validators import MaxValueValidator, MinValueValidator
from material.models import Material

####### MODELS US44############
class Ambulancia(models.Model):

    desactivada = 0
    activa = 1
    preparada  = 2
    en_viaje = 3
    estados_ambulancias = [
        (desactivada, 'Desactivada'),
        (activa, 'Activa'),
        (preparada, 'Preparada'),
        (en_viaje, 'En viaje')

    ]
    nombre = models.CharField(max_length=255, null=False, unique=True)
    estado = models.IntegerField(choices=estados_ambulancias, default=desactivada)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, unique=True)
    fecha_mod = models.DateField(null=False, default=timezone.now())

####### MODELS US44############



######## MODELS US25########
class Viaje(models.Model):
    ambulancia = models.ForeignKey(Ambulancia,on_delete=models.CASCADE)
    revision_material = models.ForeignKey(Revision,on_delete=models.CASCADE)#revision mas reciente
    fecha_inicio = models.DateTimeField()
    fecha_terminado = models.DateTimeField()

class MaterialUsado(models.Model):
    nombre = models.ForeignKey(Material,on_delete=models.CASCADE)#foreign key
    cantidad_usado = models.IntegerField(null=False, validators=[MaxValueValidator(10000), MinValueValidator(0)])
    viaje = models.ForeignKey(Viaje,on_delete=models.CASCADE)

######## MODELS US25########

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
    estados_ambulancias = [
        (desactivada, 'Desactivada'),
        (activa, 'Activa'),
    ]
    nombre = models.CharField(max_length=255, null=False, unique=True)
    estado = models.IntegerField(choices=estados_ambulancias, default=desactivada)

    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, unique=True, related_name='inventario')
    botiquin = models.ForeignKey(Inventario, on_delete=models.CASCADE, unique=True, related_name='botiquin')
    monitor = models.ForeignKey(Inventario, on_delete=models.CASCADE, unique=True, related_name='monitor')

    ambulancia_lista = models.BooleanField(default=False)
    inventario_listo = models.BooleanField(default=False)
    botiquin_listo = models.BooleanField(default=False)
    monitor_listo = models.BooleanField(default=False)

    objetivo_gasolina = 100
    objetivo_liquido_frenos = 100
    objetivo_aceite_motor = 100
    objetivo_aceite_direccion = 100
    objetivo_anticongelante = 100
    objetivo_kilometraje = 0
    objetivo_liquido_limpiaparabrisas = 100

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
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)

######## MODELS US25########

#### MODELS US28 ####
class Activables(models.Model):
    cantidad = models.IntegerField(null=False)
    fecha = models.DateTimeField(null=False, default=timezone.now())
#### MODELS US28 ####
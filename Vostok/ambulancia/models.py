from django.db import models
from inventario.models import Inventario
from django.utils import timezone

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

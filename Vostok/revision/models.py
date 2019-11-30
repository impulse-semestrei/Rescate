from django.db import models
from django.utils import timezone
from django.conf import settings

######## MODEL US41 ########

class Revision(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=False, default=timezone.now)
    observaciones = models.TextField(max_length=250)

######## MODEL US41 ########

####### Model US-29############
class RevisionAmbulancia(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=False, default=timezone.now)
    ambulancia = models.ForeignKey('ambulancia.Ambulancia', on_delete=models.CASCADE)
    gasolina = models.IntegerField()
    liquido_frenos = models.IntegerField()
    aceite_motor = models.IntegerField()
    aceite_direccion = models.IntegerField()
    anticongelante = models.IntegerField()
    kilometraje = models.IntegerField()
    liquido_limpiaparabrisas = models.IntegerField()
    observaciones = models.TextField(max_length=250)
######## MODEL US-29 ########

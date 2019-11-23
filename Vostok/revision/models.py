from django.db import models
from django.utils import timezone

######## MODEL US41 ########

class Revision(models.Model):
    nombre_paramedico = models.CharField(max_length=100, null=False)
    email_paramedico = models.CharField(max_length=100, null=False)
    fecha = models.DateTimeField(null=False, default=timezone.now)
    observaciones = models.TextField(max_length=250)

######## MODEL US41 ########

####### Model US-29############
class RevisionAmbulancia(models.Model):
    nombre_paramedico = models.CharField(max_length=100, null=False)
    email_paramedico = models.CharField(max_length=100, null=False)
    fecha = models.DateTimeField(null=False, default=timezone.now)
    ambulancia = models.ForeignKey('ambulancia.Ambulancia', on_delete=models.CASCADE)
    gasolina = models.IntegerField()
    liquido_frenos = models.IntegerField()
    observaciones = models.TextField(max_length=250)
######## MODEL US-29 ########
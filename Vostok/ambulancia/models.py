from django.db import models
from inventario.models import Inventario

# Create your models here.
class Ambulancia(models.Model):
    nombre = models.CharField(max_length=255,null=False, unique=True)
    status = models.BooleanField(default=True)
    inventario = models.ForeignKey(Inventario,on_delete=models.CASCADE)

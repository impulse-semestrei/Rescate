from django.db import models

######## MODEL US36 ########

class Material(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False)
    descripcion = models.TextField(null=False)

######## MODEL US36 ########




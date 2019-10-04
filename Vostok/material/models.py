from django.db import models

######## US36 ########


class Material(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False)
    descripcion = models.TextField(null=False)


######## US36 ########
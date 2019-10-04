from django.db import models

class Material(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False)
    descripcion = models.TextField(null=False)

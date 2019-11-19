from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_anon = models.BooleanField(default=True)
    is_voluntario = models.BooleanField(default=False)
    is_administrador = models.BooleanField(default=False)
    is_adminplus = models.BooleanField(default=False)

    date_of_birth = models.DateField(null=True)
    cellphone = models.TextField(null=True, max_length=15)


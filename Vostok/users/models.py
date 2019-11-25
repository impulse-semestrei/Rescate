from django.contrib.auth.models import AbstractUser
from django.db import models


turnoChoices=[
    (1, 'Nocturno Viernes'),
    (2, 'Diurno Sábado'),
    (3, 'Nocturno Sábado'),
    (4, 'Diurno Domingo'),
    (5, 'Nocturno Domingo'),

]

### MODELS US12 ###
class CustomUser(AbstractUser):
    is_anon = models.BooleanField(default=True)
    is_voluntario = models.BooleanField(default=False)
    is_administrador = models.BooleanField(default=False)
    is_adminplus = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    cellphone = models.TextField(null=True, max_length=15)
    turno = models.IntegerField(choices=turnoChoices,default=None,null=True)
### MODELS US12 ##


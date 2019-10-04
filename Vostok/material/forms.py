from django.forms import ModelForm
from .models import Material


######## US36 ########

class CrearMaterial(ModelForm):
    class Meta:
        model = Material
        fields = ['nombre', 'descripcion']


######## US36 ########

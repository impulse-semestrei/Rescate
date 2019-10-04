from django.forms import ModelForm
from .models import Material


######## FORM US36 ########

class CrearMaterial(ModelForm):
    """
    Forma para crear material
    """
    class Meta:
        model = Material
        fields = ['nombre', 'descripcion']


######## FORM US36 ########

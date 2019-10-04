from django.forms import ModelForm
from .models import Material

class CrearMaterial(ModelForm):
    class Meta:
        model = Material
        fields = ['nombre', 'descripcion']

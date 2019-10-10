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

    def __init__(self):
        super().__init__()
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'


######## FORM US36 ########

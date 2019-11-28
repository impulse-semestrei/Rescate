from django.forms import ModelForm
from .models import Material


######## FORM US36 ########

class CrearMaterial(ModelForm):
    """
    Forma para crear material
    """
    class Meta:
        model = Material
        fields = ['codigo','nombre', 'descripcion','cantidad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'
        self.fields['cantidad'].widget.attrs['class'] = 'form-control'

######## FORM US36 ########

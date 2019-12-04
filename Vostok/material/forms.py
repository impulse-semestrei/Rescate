from django import forms
from django.forms import ModelForm
from .models import Material


######## FORM US36 ########

class CrearMaterial(ModelForm):
    """
    Forma para crear material
    """
    descripcion = forms.CharField(label='Descripción')
    cantidad = forms.CharField(label='Cantidad Ideal')

    class Meta:
        model = Material
        fields = ['nombre', 'descripcion','cantidad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'
        self.fields['cantidad'].widget.attrs['class'] = 'form-control'

######## FORM US36 ########

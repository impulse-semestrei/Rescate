from django.forms import ModelForm,Form
from .models import Inventario

####### FORM US04############
class crearInventarioForm(ModelForm):
    class Meta:
        model = Inventario
        fields=['nombre']

####### FORMS US04############

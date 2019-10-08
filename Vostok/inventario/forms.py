from django.forms import ModelForm,Form
from .models import Inventario

####### FORMS US-04############
class crearInventarioForm(ModelForm):
    class Meta:
        model = Inventario
        fields=['nombre']

####### FORMS US-04############

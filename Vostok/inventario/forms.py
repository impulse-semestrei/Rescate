from django import forms
from .models import Inventario

####### FORM US04############
class crearInventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields=['nombre']

####### FORMS US04############


class deleteInventarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)

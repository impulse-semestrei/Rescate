from django import forms
from .models import Ambulancia
from inventario.models import Inventario
from inventario.models import Inventario
from django.forms.widgets import TextInput
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import get_object_or_404, render_to_response


####### FORM US44############


class CrearAmbulancia(forms.ModelForm):
    class Meta:
        model = Ambulancia
        fields = ['nombre', 'inventario',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['inventario'].widget.attrs['class'] = 'form-control'
        self.fields['inventario'].queryset = Inventario.objects.filter()
        self.fields['inventario'].label_from_instance = lambda obj: "%s " % obj.nombre


####### FORMS US44############

####### FORMS US26############
class CambiarEstado(forms.ModelForm):
    class Meta:
        model = Ambulancia
        fields = ['estado', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].widget.attrs['class'] = 'form-control'





####### FORMS US26############
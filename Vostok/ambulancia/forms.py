from django import forms
from .models import Ambulancia
from inventario.models import Inventario
from inventario.models import Inventario
from django.core.exceptions import ObjectDoesNotExist, ValidationError

####### FORM US44############


class CrearAmbulancia(forms.ModelForm):
    class Meta:
        model = Ambulancia
        fields = ['nombre', 'inventario']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['inventario'].widget.attrs['class'] = 'form-control'
        self.fields['inventario'].queryset = Inventario.objects.all()
        self.fields['inventario'].label_from_instance = lambda obj: "%s " % obj.nombre


####### FORMS US44############

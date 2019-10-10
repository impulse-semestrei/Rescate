<<<<<<< HEAD
from django import forms
from .models import Inventario
=======
from django.forms import ModelForm, CharField, Form, IntegerField, Field
from .models import Inventario, InventarioMaterial
from material.models import Material
from django.core.validators import MinValueValidator
from django.core.exceptions import ObjectDoesNotExist, ValidationError

>>>>>>> 318f7ba2de846503cfd84d1339d1bd0619a6e2a9

####### FORM US04############
class crearInventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields=['nombre']

<<<<<<< HEAD
####### FORMS US04############


class deleteInventarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
=======
####### FORMS US-04############


######## FORMS US1 ########


class AgregarMaterialInventario(Form):
    material = CharField(max_length=100)
    cantidad = IntegerField(min_value=0)

    def clean_material(self):
        nombre = self.cleaned_data['material']
        try:
            material = Material.objects.get(nombre=nombre)
        except ObjectDoesNotExist:
            raise ValidationError('Material no existente')
        return material


######## FORMS US1 ########
>>>>>>> 318f7ba2de846503cfd84d1339d1bd0619a6e2a9

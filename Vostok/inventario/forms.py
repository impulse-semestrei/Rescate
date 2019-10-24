from django import forms
from .models import Inventario
from django.forms import ModelForm, CharField, Form, IntegerField, Field, TextInput, NumberInput
from .models import Inventario, InventarioMaterial
from material.models import Material
from django.core.validators import MinValueValidator
from django.core.exceptions import ObjectDoesNotExist, ValidationError


####### FORM US04############
class crearInventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre']

####### FORMS US04############


class deleteInventarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)

####### FORMS US-04############


######## FORMS US1 ########


class AgregarMaterialInventario(Form):
    material = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    cantidad = IntegerField(min_value=0, widget=NumberInput(attrs={'class': 'form-control'}))


    def clean_material(self):
        nombre = self.cleaned_data['material']
        try:
            material = Material.objects.get(nombre=nombre)
        except ObjectDoesNotExist:
            raise ValidationError('Material no existente')
        return material


######## FORMS US1 ########


######## FORMS US2 ########


class EditarMaterialInventario(Form):

    cantidad = IntegerField(min_value=0, widget=NumberInput(attrs={'class': 'form-control'}))


######## FORMS US2 ########
from django.forms import ModelForm, CharField, Form, IntegerField, Field
from .models import Inventario, InventarioMaterial
from material.models import Material
from django.core.validators import MinValueValidator
from django.core.exceptions import ObjectDoesNotExist, ValidationError


####### FORM US04############
class crearInventarioForm(ModelForm):
    class Meta:
        model = Inventario
        fields=['nombre']

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

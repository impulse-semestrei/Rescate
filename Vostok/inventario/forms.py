from django.forms import ModelForm
from .models import Inventario, InventarioMaterial

####### FORMS US-04############
class crearInventarioForm(ModelForm):
    class Meta:
        model = Inventario
        fields=['nombre']

####### FORMS US-04############


######## FORMS US1 ########


class AgregarMaterialInventario(ModelForm):
    class Meta:
        model = InventarioMaterial
        fields = ['material', 'cantidad']


######## FORMS US1 ########

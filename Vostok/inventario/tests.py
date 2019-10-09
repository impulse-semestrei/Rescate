from django.test import TestCase
from django.urls import reverse
from .models import Inventario, InventarioMaterial
from material.models import Material
from .forms import AgregarMaterialInventario

# Create your tests here.


######## TESTS US1 ########


class AgregarMaterialInventarioTestCase(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.material = Material.objects.create(nombre='curita', descripcion='proteccion de herida')

    def test_url_correct(self):
        """
        Regresar un codigo 200
        """
        response = self.client.get(reverse('inventario:agregar_material_inventario', args={self.inventario.id}))
        self.assertEqual(response.status_code, 200)

    def test_form_correct(self):
        """
        La forma es valida para guardarse en la bd
        """
        data = {
            'material': self.material.nombre,
            'cantidad': 2,
        }
        form = AgregarMaterialInventario(data)
        self.assertTrue(form.is_valid())
        material = form.cleaned_data['material']
        cantidad = form.cleaned_data['cantidad']
        InventarioMaterial.objects.create(inventario=self.inventario, material=material, cantidad=cantidad)
        self.assertEqual(self.inventario.materiales.count(), 1)
        self.assertEqual(self.inventario.materiales.first().nombre, self.material.nombre)

    def test_form_incomplete(self):
        """
        La forma es valida para guardarse en la bd
        """
        data = {
            'material': '',
            'cantidad': 2,
        }
        form = AgregarMaterialInventario(data)
        self.assertFalse(form.is_valid())



######## TESTS US1 ########

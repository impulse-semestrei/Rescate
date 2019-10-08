from django.test import TestCase
from inventario.forms import crearInventarioForm
from inventario.models import Inventario
from material.forms import CrearMaterial
from material.models import Material


####### TESTS US-04############

class InventarioTestCase(TestCase):
    def test_NoSession(self):
        response = self.client.get('/inventario/crear/')
        self.assertEqual(response.status_code, 302)

    def test_form_inventario_valid(self):
        self.Materiales = Material.objects.create(nombre='Tapabocas', descripcion='Cubre la boca y nariz')
        almacen = {
            'nombre': 'botiquin',

        }

        form = crearInventarioForm(almacen)
        self.assertTrue(form.is_valid())

    def test_form_inventario_invalid(self):
        Material.objects.create(nombre='Tapabocas', descripcion='Cubre la boca y nariz')
        almacen = {
            'nombre': '',

        }

        form = crearInventarioForm(almacen)
        self.assertFalse(form.is_valid())

    def testCreateInventario(self):
        Inventario.objects.create(nombre="tempInventario")
        self.assertTrue(Inventario.objects.filter(nombre="tempInventario"))

####### TESTS US-04############

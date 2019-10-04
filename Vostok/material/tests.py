from django.test import TestCase
from django.urls import reverse
from .forms import CrearMaterial
from .models import Material


######## US36 ########


class CrearMaterialTestCase(TestCase):
    def test_url_correct(self):
        response = self.client.get(reverse('material:crear'))
        self.assertEqual(response.status_code, 200)

    def test_form_correct(self):
        data = {
            'nombre': 'curita',
            'descripcion': 'proteccion de herida',
        }
        form = CrearMaterial(data)
        self.assertTrue(form.is_valid())

    def test_form_incorrect(self):
        data = {
            'nombre': '',
            'descripcion': 'proteccion de herida',
        }
        form = CrearMaterial(data)
        self.assertFalse(form.is_valid())

    def test_form_not_unique(self):
        Material.objects.create(nombre='curita', descripcion='proteccion de herida')
        data = {
            'nombre': 'curita',
            'descripcion': 'proteccion de herida',
        }
        form = CrearMaterial(data)
        self.assertFalse(form.is_valid())


######## US36 ########
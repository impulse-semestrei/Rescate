from django.test import TestCase
from inventario.models import Inventario
from .models import Ambulancia
from .views import crear_ambulancia
from .forms import CrearAmbulancia
from django.urls import reverse

####### TEST US44############
class CrearAmbulanciaTest(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")

    def test_url(self):

        response = self.client.get(reverse('ambulancia:crear'))
        self.assertEqual(response.status_code, 200)

    def test_form(self):
        data = {
            'nombre': 'Azul510',
            'inventario': self.inventario.id,
        }
        form = CrearAmbulancia(data)
        self.assertTrue(form.is_valid())


    def test_model(self):
        self.almacen= Ambulancia.objects.create(nombre='ambulancia', inventario=self.inventario)
        self.assertTrue(Ambulancia.objects.filter(inventario_id=self.inventario))
####### TEST US44############

####### TEST US45############
class EditarAmbulancia(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
    def test_editarMaterialName(self):
            Ambulancia.objects.create(nombre='Test', inventario=self.inventario)
            self.client.get('ambulancia:editar_ambulancia', )

####### TEST US45############
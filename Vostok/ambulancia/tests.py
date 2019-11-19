from django.test import TestCase
from inventario.models import Inventario
from .models import Ambulancia
from .views import crear_ambulancia
from .forms import CrearAmbulancia, CambiarEstado
from django.urls import reverse
from django.utils import timezone
from revision.models import RevisionAmbulancia
import json

####### TEST US44############
class CrearAmbulanciaTest(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")

    def test_url(self):

        response = self.client.get(reverse('ambulancia:crear'))
        self.assertEqual(response.status_code, 302)

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


#### TESTS US21 ####
class ChecklistAmbulanciaTestCase(TestCase):
    def setUp(self):
        inventario = Inventario.objects.create(nombre="Inventario de ambulancia")
        self.ambulancia = Ambulancia.objects.create(nombre="Ambulancia", inventario=inventario)
        self.revision = RevisionAmbulancia.objects.create(
            nombre_paramedico="paramedico",
            email_paramedico="paramedico@mail.com",
            fecha=timezone.now(),
            ambulancia=self.ambulancia,
            gasolina=80.0,
            liquido_frenos=200
        )

    def test_get(self):
        response = self.client.get(reverse('ambulancia:checklist_ambulancia', args=[self.ambulancia.id]))
        materiales = {
            'gasolina': 80.0,
            'liquido_frenos': 200
        }
        self.assertEqual(json.loads(response.content), materiales)

    def test_post(self):
        pass
#### TESTS US21 ####


####### TEST US26############
class ControlAmbulancias(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre='almacen')
        self.ambulancia = Ambulancia.objects.create(nombre='ambulancia10', inventario=self.inventario)

    def test_view(self):
        response = self.client.get(reverse('ambulancia:ver_control_ambulancias'))
        self.assertEqual(response.status_code, 200)

    def test_form(self):
        estado = {
            'estado': 3
        }
        form = CambiarEstado(estado)
        self.assertTrue(form.is_valid())

####### TEST US26############
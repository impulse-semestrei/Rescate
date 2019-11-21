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


#### TESTS US28 ####
class ChecklistAmbulanciaTestCase(TestCase):
    def setUp(self):
        inventario = Inventario.objects.create(nombre="Inventario de ambulancia")
        self.ambulancia = Ambulancia.objects.create(nombre="Ambulancia", inventario=inventario)
        self.revision = RevisionAmbulancia.objects.create(
            nombre_paramedico="paramedico",
            email_paramedico="paramedico@mail.com",
            fecha=timezone.now(),
            ambulancia=self.ambulancia,
            gasolina=80,
            liquido_frenos=200
        )

    def test_get(self):
        referencia = {
            "elementos": [
                {
                    "nombre": "gasolina",
                    "id": 1,
                    "objetivo": 100,
                    "cantidad": 80
                },
                {
                    "nombre": "liquido de frenos",
                    "id": 2,
                    "objetivo": 50,
                    "cantidad": 200
                }
            ]
        }
        respuesta = self.client.get(reverse('ambulancia:checklist_ambulancia', args=[self.ambulancia.id]))
        self.assertEqual(json.loads(respuesta.content), referencia)



class ListaAmbulanciasTestCase(TestCase):
    def setUp(self):
        inventario1 = Inventario.objects.create(nombre="Inventario de ambulancia 1")
        self.ambulancia1 = Ambulancia.objects.create(nombre="Ambulancia 1", inventario=inventario1)
        inventario2 = Inventario.objects.create(nombre="Inventario de ambulancia 2")
        self.ambulancia2 = Ambulancia.objects.create(nombre="Ambulancia 2", inventario=inventario2)
        inventario3 = Inventario.objects.create(nombre="Inventario de ambulancia 3")
        self.ambulancia3 = Ambulancia.objects.create(nombre="Ambulancia 3", inventario=inventario3)

    def test_get(self):
        referencia = {
            "ambulancias": [
                {
                    "nombre": "Ambulancia",
                    "id": 1,
                    "idInventario": 1
                },
                {
                    "nombre": "Ambulancia 2",
                    "id": 2,
                    "idInventario": 2
                },
                {
                    "nombre": "Ambulancia 3",
                    "id": 3,
                    "idInventario": 3
                }
            ]
        }
        respuesta = self.client.get(reverse('ambulancia:lista_ambulancias'))
        self.assertEqual(json.loads(respuesta), referencia)


#### TESTS US28 ####


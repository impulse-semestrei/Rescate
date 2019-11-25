from django.test import TestCase
from inventario.models import Inventario
from .models import Ambulancia, Viaje
from .views import crear_ambulancia
from .forms import CrearAmbulancia, CambiarEstado
from django.urls import reverse
from django.utils import timezone
from revision.models import RevisionAmbulancia
import json
from revision.models import Revision

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


######## TESTS US22 ########
class VerMaterialUsadoTestCase(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
    def test_verMaterialURL(self):
        ambulancia = Ambulancia.objects.create(nombre='Test', inventario=self.inventario)
        rev = Revision.objects.create(nombre_paramedico='lore', email_paramedico='vostok@itesm.mx', fecha='2001-09-28 02:00:00')
        viaje = Viaje.objects.create(fecha_inicio='2001-09-28 01:00:00' , fecha_terminado= '2001-09-28 02:00:00', ambulancia_id=ambulancia.id , revision_material_id=rev.id)
        response = self.client.get(reverse('ambulancia:materiales_usados', args={viaje.id}))
        self.assertEqual(response.status_code, 302)

######## TESTS US22 ########


####### TEST US26############
class ControlAmbulancias(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre='almacen')
        self.ambulancia = Ambulancia.objects.create(nombre='ambulancia10', inventario=self.inventario)

    def test_view(self):
        response = self.client.get(reverse('ambulancia:ver_control_ambulancias'))
        self.assertEqual(response.status_code, 302)

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
            "materiales": [
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
        inventario1.save()
        self.ambulancia1 = Ambulancia.objects.create(nombre="Ambulancia 1", inventario=inventario1)
        self.ambulancia1.save()


    def test_get(self):
        referencia = {
            "ambulancias": [
                {
                    "nombre": "Ambulancia 1",
                    "id": 6,
                    "idInventario": 8

                },

            ]
        }
        respuesta = self.client.get(reverse('ambulancia:lista_ambulancias'))
        self.assertEqual(json.loads(respuesta.content), referencia)


#### TESTS US28 ####

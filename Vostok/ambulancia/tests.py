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
from users.models import CustomUser

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
        self.ambulancia = Ambulancia.objects.create(nombre='Test', inventario=self.inventario)
        self.user = CustomUser.objects.create(is_anon=False,
                                              is_voluntario=False,
                                              is_administrador=False,
                                              is_adminplus=True,
                                              date_of_birth='2019-01-01',
                                              turno=1,
                                              )
        self.rev = Revision.objects.create(usuario=self.user, fecha=timezone.now(), observaciones="a")

        self.viaje = Viaje.objects.create(fecha_inicio='2001-09-28 01:00:00' , fecha_terminado= '2001-09-28 02:00:00', ambulancia_id=self.ambulancia.id , revision_material=self.rev)
    def test_verMaterialURL(self):
        response = self.client.get(reverse('ambulancia:materiales_usados', args={self.viaje.id}))
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
            'estado': 'Activa'
        }
        form = CambiarEstado(estado)
        self.assertFalse(form.is_valid())

####### TEST US26############


#### TESTS US28 ####
class ChecklistAmbulanciaTestCase(TestCase):
    def setUp(self):
        inventario = Inventario.objects.create(nombre="Inventario de ambulancia")
        self.ambulancia = Ambulancia.objects.create(nombre="Ambulancia", inventario=inventario)
        self.user = CustomUser.objects.create(is_anon=False,
                                              is_voluntario=False,
                                              is_administrador=False,
                                              is_adminplus=True,
                                              date_of_birth='2019-01-01',
                                              turno=1,
                                              )
        self.revision = RevisionAmbulancia.objects.create(ambulancia=self.ambulancia,gasolina=1,liquido_frenos=1,aceite_motor=1,aceite_direccion=1,anticongelante=1,kilometraje=1,liquido_limpiaparabrisas=1,usuario=self.user, fecha=timezone.now(), observaciones="a")

    def test_get(self):
        referencia = {
            "materiales": [
                {
                    "nombre": "Gasolina",
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
        self.assertNotEqual(json.loads(respuesta.content), referencia)



class ListaAmbulanciasTestCase(TestCase):
    def setUp(self):
        inventario1 = Inventario.objects.create(nombre="Inventario de ambulancia 1")
        inventario1.save()
        self.ambulancia1 = Ambulancia.objects.create(nombre="Ambulancia 1", inventario=inventario1)
        self.ambulancia1.save()


    def test_get(self):
        referencia = {
            "ambulancias": [

            ]
        }
        respuesta = self.client.get(reverse('ambulancia:lista_ambulancias'))
        self.assertEqual(json.loads(respuesta.content), referencia)


#### TESTS US28 ####

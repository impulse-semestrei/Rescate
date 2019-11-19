from django.test import TestCase
from inventario.models import Inventario
from .models import Ambulancia, Viaje
from .views import crear_ambulancia
from .forms import CrearAmbulancia
from django.urls import reverse
from revision.models import Revision

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


######## TESTS US22 ########
class VerMaterialUsadoTestCase(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
    def test_verMaterialURL(self):
        ambulancia = Ambulancia.objects.create(nombre='Test', inventario=self.inventario)
        rev = Revision.objects.create(nombre_paramedico='lore', email_paramedico='vostok@itesm.mx', fecha='2001-09-28 02:00:00')
        viaje = Viaje.objects.create(fecha_inicio='2001-09-28 01:00:00' , fecha_terminado= '2001-09-28 02:00:00', ambulancia_id=ambulancia.id , revision_material_id=rev.id)
        response = self.client.get(reverse('ambulancia:materiales_usados', args={viaje.id}))
        self.assertEqual(response.status_code, 200)

######## TESTS US22 ########
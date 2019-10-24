from django.test import TestCase
from inventario.forms import crearInventarioForm
from material.forms import CrearMaterial
from django.urls import reverse
from .models import Inventario, InventarioMaterial
from material.models import Material
from django.utils import timezone
from .views import delete_inventario, eliminar_material_inventario
from .forms import AgregarMaterialInventario
import json
from .forms import AgregarMaterialInventario, EditarMaterialInventario

# Create your tests here.


######## TESTS US1 ########


class AgregarMaterialInventarioTestCase(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.material = Material.objects.create(nombre='curita', descripcion='proteccion de herida')

    def test_url_correct(self):
        """
        Regresar un codigo 302 porque el usuario no está logueado y debe redireccionarse
        """
        response = self.client.get(reverse('inventario:agregar_material_inventario', args={self.inventario.id}))
        self.assertEqual(response.status_code, 302)

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


class verInventarioTest(TestCase):
    def test_url(self):
        response = self.client.get('/inventario/ver/')
        self.assertEqual(response.status_code, 200)


####### TESTS US-06############
class deleteInventarioTest(TestCase):
    def test_url(self):
        inventario = Inventario.objects.create(nombre="Test")
        response=self.client.get('/inventario/delete/'+str(inventario.id)+'/')
        self.assertEqual(response.status_code, 200)

    def test_model(self):
        inventario = Inventario.objects.create(nombre="Test")
        status_before = inventario.status
        date_before = inventario.fechaMod

        inventario.status = False

        inventario.fechaMod = timezone.now()
        inventario.save()

        status_after = inventario.status
        date_after = inventario.fechaMod

        self.assertNotEqual(status_before, status_after)
        self.assertNotEqual(date_before, date_after)

    def test_view(self):
        inventario = Inventario.objects.create(nombre="Testing_view")

        inventario.status = False
        delete_inventario(self.client.get('/inventario/delete/'+str(inventario.id)+'/'), str(inventario.id))

        self.assertFalse(inventario.status)


####### TESTS US-06############


####### TESTS US-05############
class VerMaterialTestCase(TestCase):
    def test_MaterialInventarioURL(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.material = Material.objects.create(nombre='curita', descripcion='proteccion de herida')
        self.MatInv = InventarioMaterial.objects.create(inventario=self.inventario, material=self.material, cantidad=4)

        response = self.client.get(reverse('inventario:material_inventario', args={self.inventario.id}))
        self.assertEqual(response.status_code, 200)

####### TESTS US-05############


######## TEST US-03 ########
class EliminarMaterialInventarioTestCase(TestCase):
    def test_eliminarMaterial(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.material = Material.objects.create(nombre='curita', descripcion='proteccion de herida')
        self.MatInv = InventarioMaterial.objects.create(inventario=self.inventario, material=self.material, cantidad=4)
        self.MatInv.delete()
        self.assertFalse(InventarioMaterial.objects.filter(material=self.MatInv.material))
######## TEST US-03 ########

#### TESTS US21 ####
class ChecklistTestCase(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="inventario")
        self.material1 = Material.objects.create(
            nombre="material1",
            descripcion="material1",
            cantidad=1
        )
        self.material2 = Material.objects.create(
            nombre="material2",
            descripcion="material2",
            cantidad=2
        )
        InventarioMaterial.objects.create(
            inventario=self.inventario,
            material=self.material1,
            fecha=timezone.now(),
            cantidad=1
        )
        InventarioMaterial.objects.create(
            inventario=self.inventario,
            material=self.material2,
            fecha=timezone.now(),
            cantidad=2
        )

    def test_response(self):
        response = self.client.get(reverse('inventario:checklist', args=[self.inventario.id]))
        materiales = json.loads(response.content)
        self.assertJSONEqual(
            materiales,
            {
                "materiales": [
                    {
                        "id": self.material1.id,
                        "nombre": self.material1.nombre,
                        "cantidad": 1
                    },
                    {
                        "id": self.material2.id,
                        "nombre": self.material2.nombre,
                        "cantidad": 2
                    }
                ]
            }
        )

    def test_request(self):
        datos = json.dumps(
            {
                "materiales": [
                    {
                        "id": self.material1.id,
                        "nombre": self.material1.nombre,
                        "cantidad": 2
                    },
                    {
                        "id": self.material2.id,
                        "nombre": self.material2.nombre,
                        "cantidad": 3
                    }
                ]
            }
        )
        response = self.client.post(reverse('inventario:checklist', args=[self.inventario.id]), {"datos": datos})
        self.assertJSONEqual(json.loads(response.content), {"status": "OK"})
        self.assertTrue(InventarioMaterial.objects.all().count(), 4)
#### TESTS US21 ####


######## TEST US-02 ########

class EditarMaterialInventarioTest(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.material = Material.objects.create(nombre='curita', descripcion='proteccion de herida')
        self.MatInv = InventarioMaterial.objects.create(
            inventario=self.inventario,
            material=self.material,
            cantidad=4
        )

    def test_form_correct(self):
        data = {
            'cantidad': 2,
        }
        form = EditarMaterialInventario(data)
        self.assertTrue(form.is_valid())
        cant = form.cleaned_data['cantidad']
        self.MatInv.cantidad = cant
        self.MatInv.save()
        self.assertTrue(
            InventarioMaterial.objects.filter(material=self.MatInv.material, inventario=self.MatInv.inventario))


######## TEST US-02 ########

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
from revision.models import Revision
from users.models import CustomUser

# Create your tests here.


######## TESTS US1 ########


class AgregarMaterialInventarioTestCase(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.material = Material.objects.create(nombre='curita', descripcion='proteccion de herida', cantidad=3)

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
        usuario = CustomUser.objects.create(is_anon=False, is_adminplus=True)
        revision = Revision.objects.create(usuario=usuario, fecha=timezone.now(), observaciones='Observacion')
        InventarioMaterial.objects.create(inventario=self.inventario, material=material, cantidad=cantidad, revision=revision)
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
    def test_no_session(self):
        response = self.client.get('/inventario/crear/')
        self.assertEqual(response.status_code, 302)

    def test_form_inventario_valid(self):
        almacen = {
            'nombre': 'botiquin',
        }
        form = crearInventarioForm(almacen)
        self.assertTrue(form.is_valid())

    def test_form_inventario_invalid(self):
        almacen = {
            'nombre': '',
        }
        form = crearInventarioForm(almacen)
        self.assertFalse(form.is_valid())

    def test_create_inventario(self):
        Inventario.objects.create(nombre="tempInventario")
        self.assertTrue(Inventario.objects.filter(nombre="tempInventario"))


####### TESTS US-04############


class VerInventarioTestCase(TestCase):
    def test_url(self):
        response = self.client.get('/inventario/ver/')
        self.assertEqual(response.status_code, 302)


####### TESTS US-06############
class DeleteInventarioTestCase(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="Test")

    def test_url(self):
        response=self.client.get('/inventario/delete/'+str(self.inventario.id)+'/')
        self.assertEqual(response.status_code, 302)

    def test_model(self):
        status_before = self.inventario.status

        self.inventario.status = False
        self.inventario.save()

        status_after = self.inventario.status

        self.assertNotEqual(status_before, status_after)


####### TESTS US-06############


####### TESTS US-05############
class VerMaterialTestCase(TestCase):
    def test_url(self):
        inventario = Inventario.objects.create(nombre="Test")
        response = self.client.get(reverse('inventario:material_inventario', args={inventario.id}))
        self.assertEqual(response.status_code, 302)

####### TESTS US-05############


######## TEST US-03 ########
class EliminarMaterialInventarioTestCase(TestCase):
    def test_eliminarMaterial(self):
        usuario = CustomUser.objects.create(is_anon=False, is_adminplus=True)
        revision = Revision.objects.create(usuario=usuario,fecha=timezone.now(), observaciones='Observacion')
        inventario = Inventario.objects.create(nombre="almacen")
        material = Material.objects.create(codigo='codigo1', nombre='curita', descripcion='proteccion de herida', cantidad=4)
        mat_inv = InventarioMaterial.objects.create(inventario=inventario, material=material, cantidad=4, revision=revision)
        mat_inv.delete()
        self.assertFalse(InventarioMaterial.objects.filter(material=mat_inv.material))
######## TEST US-03 ########


#### TESTS US21 ####
class ChecklistTestCase(TestCase):
    def setUp(self):
        usuario = CustomUser.objects.create(is_anon=False, is_adminplus=True)
        revision = Revision.objects.create(usuario=usuario, fecha=timezone.now(), observaciones='Observacion')
        self.inventario = Inventario.objects.create(nombre="inventario")
        self.material1 = Material.objects.create(
            codigo='codigo1',
            nombre="material1",
            descripcion="material1",
            cantidad=1
        )
        self.material2 = Material.objects.create(
            codigo='codigo2',
            nombre="material2",
            descripcion="material2",
            cantidad=2
        )
        InventarioMaterial.objects.create(

            inventario=self.inventario,
            material=self.material1,
            cantidad=1,
            revision=revision
        )
        InventarioMaterial.objects.create(
            inventario=self.inventario,
            material=self.material2,
            cantidad=2,
            revision=revision
        )

    def test_response(self):
        response = self.client.get(reverse('inventario:checklist', args=[self.inventario.id]))
        materiales = {
                        "materiales": [
                            {
                                "id": self.material1.id,
                                "nombre": self.material1.nombre,
                                "cantidad": 1,
                                "objetivo": 1,
                                "medida": "Cantidad"
                            },
                            {
                                "id": self.material2.id,
                                "nombre": self.material2.nombre,
                                "cantidad": 2,
                                "objetivo": 2,
                                "medida": "Cantidad"
                            }
                        ]
                    }
        self.assertEqual(json.loads(response.content), materiales)
#### TESTS US21 ####


######## TEST US-02 ########

class EditarMaterialInventarioTest(TestCase):
    def setUp(self):
        usuario = CustomUser.objects.create(is_anon=False, is_adminplus=True)
        revision = Revision.objects.create(usuario=usuario, fecha=timezone.now(), observaciones='Observacion')
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.material = Material.objects.create(codigo='codigo1', nombre='curita', descripcion='proteccion de herida', cantidad=1)
        self.MatInv = InventarioMaterial.objects.create(
            inventario=self.inventario,
            material=self.material,
            cantidad=4,
            revision=revision
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

from django.test import TestCase
from inventario.models import Inventario
from ambulancia.models import Ambulancia
from revision.models import Revision
from django.urls import reverse

# Create your tests here.
####### TESTS US-41############


class VerMaterialTestCase(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.inventario.save()
        self.ambulancia = Ambulancia.objects.create(nombre="ambulancia", inventario=self.inventario)
        self.ambulancia.save()
        self.revision = Revision.objects.create(inventario=self.inventario)
        self.revision.save()

    def test_RevisionesURL(self):

        response = self.client.get(reverse('revision:revisiones', args={self.ambulancia.id}))
        self.assertEqual(response.status_code, 302)

    def test_model(self):
        self.assertTrue(Revision.objects.filter(id=self.revision.id))




####### TESTS US-41############
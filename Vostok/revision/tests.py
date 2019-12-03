from django.test import TestCase
from inventario.models import Inventario
from ambulancia.models import Ambulancia
from revision.models import Revision, RevisionAmbulancia
from django.urls import reverse
from django.utils import timezone
from users.models import CustomUser

# Create your tests here.
####### TESTS US-41############


class VerRevisionTestCase(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.inventario.save()
        self.ambulancia = Ambulancia.objects.create(nombre="ambulancia", inventario=self.inventario)
        self.ambulancia.save()
        self.user = CustomUser.objects.create(is_anon=False,
                                              is_voluntario=False,
                                              is_administrador=False,
                                              is_adminplus=True,
                                              date_of_birth='2019-01-01',
                                              turno=1,
        )
        self.revision = Revision.objects.create(usuario=self.user,fecha=timezone.now(), observaciones="a")
        self.revision.save()

    def test_RevisionesURL(self):
        response = self.client.get(reverse('revision:revisiones', args={self.ambulancia.id}))
        print(response.status_code)
        self.assertEqual(response.status_code, 302)

    def test_model(self):
        self.assertTrue(Revision.objects.filter(id=self.revision.id))




####### TESTS US-41############

class VerDetalleRevision(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.inventario.save()
        self.ambulancia = Ambulancia.objects.create(nombre="ambulancia", inventario=self.inventario)
        self.ambulancia.save()
        self.user = CustomUser.objects.create(is_anon=False,
                                              is_voluntario=False,
                                              is_administrador=False,
                                              is_adminplus=True,
                                              date_of_birth='2019-01-01',
                                              turno=1,
        )
        self.revision = Revision.objects.create(usuario=self.user,fecha=timezone.now(), observaciones="a")
        self.revision.save()

    def test_url(self):
        response  = self.client.get(reverse('revision:detalle_revision', args=[self.ambulancia.id,self.revision.id]))
        self.assertEqual(response.status_code, 302)


####### TESTS US-29############
class VerEstadoAmbulancia(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.inventario.save()
        self.ambulancia = Ambulancia.objects.create(nombre="ambulancia", inventario=self.inventario)
        self.ambulancia.save()
        self.user = CustomUser.objects.create(is_anon=False,
                                              is_voluntario=False,
                                              is_administrador=False,
                                              is_adminplus=True,
                                              date_of_birth='2019-01-01',
                                              turno=1,
                                              )
        self.revision = RevisionAmbulancia.objects.create(ambulancia=self.ambulancia,gasolina=1,liquido_frenos=1,aceite_motor=1,aceite_direccion=1,anticongelante=1,kilometraje=1,liquido_limpiaparabrisas=1,usuario=self.user, fecha=timezone.now(), observaciones="a")
        self.revision.save()

    def test_RevisionAmbulanciaURL(self):
        response = self.client.get(reverse('revision:revisiones_ambulancia', args={self.ambulancia.id}))
        self.assertEqual(response.status_code, 302)

    def test_model(self):
        print(RevisionAmbulancia.objects.get(id=self.revision.id))
        self.assertTrue(RevisionAmbulancia.objects.get(id=self.revision.id))
####### TESTS US-29############

####### TESTS US-30############
class VerDetalleAmbulancia(TestCase):
    def setUp(self):
        self.inventario = Inventario.objects.create(nombre="almacen")
        self.inventario.save()
        self.ambulancia = Ambulancia.objects.create(nombre="ambulancia", inventario=self.inventario)
        self.ambulancia.save()
        self.user = CustomUser.objects.create(is_anon=False,
                                              is_voluntario=False,
                                              is_administrador=False,
                                              is_adminplus=True,
                                              date_of_birth='2019-01-01',
                                              turno=1,
                                              )
        self.revision = Revision.objects.create(usuario=self.user, fecha=timezone.now(), observaciones="a")
        self.revision.save()

    def test_URL(self):
        response = self.client.get(reverse('revision:detalle_ambulancia', args=[self.ambulancia.id, self.revision.id]))
        self.assertEqual(response.status_code, 302)
 ####### TESTS US-30############
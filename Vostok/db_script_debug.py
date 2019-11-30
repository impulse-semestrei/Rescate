from inventario.models import Inventario, InventarioMaterial
from material.models import Material
from ambulancia.models import Ambulancia
from revision.models import Revision, RevisionAmbulancia
from django.utils import timezone
from django.contrib.auth import get_user_model

InventarioMaterial.objects.all().delete()
Ambulancia.objects.all().delete()
Inventario.objects.all().delete()
Material.objects.all().delete()
Revision.objects.all().delete()

materiales = []
# Materiales de ambulancia
materiales.append(Material.objects.create(nombre="Desinfectante para manos", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Férula de tracción", descripcion="", cantidad=1, medida="Presión"))

fecha = timezone.now()

nombres = ['Azul 1', 'Azul 2', 'Azul 3', 'Azul 4', 'Azul 5']

user = get_user_model().objects.all().first()

for nombre in nombres:
    inventario = Inventario.objects.create(nombre="inventario "+nombre)
    ambulancia = Ambulancia.objects.create(nombre=nombre, inventario=inventario, estado=Ambulancia.activa)
    revision = Revision.objects.create(fecha=fecha, usuario=user)
    revision_ambulancia = RevisionAmbulancia.objects.create(
        fecha=fecha,
        ambulancia=ambulancia,
        gasolina=90,
        liquido_frenos=40,
        aceite_motor=100,
        aceite_direccion=100,
        anticongelante=100,
        kilometraje=100,
        liquido_limpiaparabrisas=100,
        usuario=user,
    )
    for material in materiales:
        InventarioMaterial.objects.create(
            inventario=inventario,
            material=material,
            cantidad=material.cantidad,
            revision=revision,
        )

ambulancia_desactivada = Ambulancia.objects.get(nombre=nombres[len(nombres) - 1])
ambulancia_desactivada.estado = Ambulancia.desactivada
ambulancia_desactivada.save()
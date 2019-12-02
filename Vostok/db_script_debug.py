from inventario.models import Inventario, InventarioMaterial
from material.models import Material
from ambulancia.models import Ambulancia, Activables
from revision.models import Revision, RevisionAmbulancia
from django.utils import timezone
from django.contrib.auth import get_user_model

InventarioMaterial.objects.all().delete()
Ambulancia.objects.all().delete()
Inventario.objects.all().delete()
Material.objects.all().delete()
Revision.objects.all().delete()
Activables.objects.all().delete()

materiales = []
# Materiales de ambulancia
materiales.append(Material.objects.create(nombre="Desinfectante para manos", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Férula de tracción", descripcion="", cantidad=1, medida="Presión"))

materialesBotiquin = []
# Materiales de botiquín
materialesBotiquin.append(Material.objects.create(nombre="Material botiquín 1", descripcion="", cantidad=1))
materialesBotiquin.append(Material.objects.create(nombre="Material botiquín 2", descripcion="", cantidad=2, medida="Porcentaje"))

materialesMonitor = []
# Materiales de monitor
materialesMonitor.append(Material.objects.create(nombre="Material monitor 1", descripcion="", cantidad=1))
materialesMonitor.append(Material.objects.create(nombre="Material monitor 2", descripcion="", cantidad=2, medida="Porcentaje"))


fecha = timezone.now()

nombres = ['Azul 1', 'Azul 2', 'Azul 3', 'Azul 4', 'Azul 5']

user = get_user_model().objects.all().first()

for nombre in nombres:
    inventario = Inventario.objects.create(nombre="inventario "+nombre)
    botiquin = Inventario.objects.create(nombre="botiquin "+nombre)
    monitor = Inventario.objects.create(nombre="monitor "+nombre)
    ambulancia = Ambulancia.objects.create(
        nombre=nombre,
        inventario=inventario,
        botiquin=botiquin,
        monitor=monitor,
        estado=Ambulancia.activa
    )
    revisionInventario = Revision.objects.create(fecha=fecha, usuario=user)
    revisionBotiquin = Revision.objects.create(fecha=fecha, usuario=user)
    revisionMonitor = Revision.objects.create(fecha=fecha, usuario=user)
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
            revision=revisionInventario,
        )
    for material in materialesBotiquin:
        InventarioMaterial.objects.create(
            inventario=botiquin,
            material=material,
            cantidad=material.cantidad,
            revision=revisionBotiquin,
        )
    for material in materialesMonitor:
        InventarioMaterial.objects.create(
            inventario=monitor,
            material=material,
            cantidad=material.cantidad,
            revision=revisionMonitor,
        )

ambulancia_desactivada = Ambulancia.objects.get(nombre=nombres[len(nombres) - 1])
ambulancia_desactivada.estado = Ambulancia.desactivada
ambulancia_desactivada.save()
Activables.objects.create(cantidad=2)
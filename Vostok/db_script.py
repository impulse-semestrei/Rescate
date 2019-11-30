from inventario.models import Inventario, InventarioMaterial
from material.models import Material
from ambulancia.models import Ambulancia, Activables
from revision.models import Revision, RevisionAmbulancia
from django.utils import timezone

InventarioMaterial.objects.all().delete()
Ambulancia.objects.all().delete()
Inventario.objects.all().delete()
Material.objects.all().delete()
Revision.objects.all().delete()
Activables.objects.all().delete()

materiales = []
# Materiales de ambulancia
materiales.append(Material.objects.create(nombre="Desinfectante para manos", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Desinfectante para superficies", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Bote de basura", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Tabla de partes", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Camilla rígida", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Tabla pediátrica", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Bloques pediátricos", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Camilla marina", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Araña", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Araña pediátrica", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Tubular", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Inmovilizador pélvico", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Base para bloques", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Bloques", descripcion="", cantidad=4))
materiales.append(Material.objects.create(nombre="Sujetadores", descripcion="", cantidad=4))
materiales.append(Material.objects.create(nombre="Férulas superiores", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Férulas inferiores", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Chaleco de extracción", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Férula de tracción", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Espátula", descripcion="", cantidad=1))

# Aquí empiezan los materiales de torundas
materiales.append(Material.objects.create(nombre="Alcohol", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Jabón quirúrgico", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Cloruro de benzalconio", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Yodopolividina", descripcion="", cantidad=1))
# Aquí terminan los materiales de torundas

materiales.append(Material.objects.create(nombre="Estetoscopio adulto", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Estetoscopio pediátrico", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Rastrillo", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Desfibrilador portátil", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Parche DEA", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Ligadura", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Caja de punzos", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Cont.rojo para punzocortantes", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Bolsas amarillas", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Bolsas rojas", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Mascarillas N95", descripcion="", cantidad=4))
materiales.append(Material.objects.create(nombre="Sábana", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Cobertor", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Sábana para quemados", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Guía de materiales peligrosos", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Tanque de oxígeno portátil", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Tarjetas TRIAGE", descripcion="", cantidad=10))
materiales.append(Material.objects.create(nombre="Caja medicamentos", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Chalecos naranjas", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Cascos de seguridad", descripcion="", cantidad=4))
materiales.append(Material.objects.create(nombre="Chaquetón de bombero", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Casco de bombero", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Collarín pediátrico", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Collarín adulto", descripcion="", cantidad=2))

# Aquí empieza el equipo de intubación
materiales.append(Material.objects.create(nombre="Hojas rectas", descripcion="", cantidad=4))
materiales.append(Material.objects.create(nombre="Estilete adulto", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Estilete pediátrico", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Hojas curvas", descripcion="", cantidad=3))
materiales.append(Material.objects.create(nombre="Mango", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Pilas (fuera del mango)", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Lubricante hidrosoluble", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Pinza Magill adulto", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Pinza Magill pediátria", descripcion="", cantidad=1))
# Aquí termina el equipo de entubación

materiales.append(Material.objects.create(nombre="Carbón activado", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Doppler fetal", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Estetoscopio de pinard", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Kit obstétrico", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Pinzas Rochester", descripcion="", cantidad=2))
materiales.append(Material.objects.create(nombre="Onfalotomo", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Tijera Mayo", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Perilla para aspiración", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Aspirador portátil", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Manguera aspirador", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Canula Yankauer", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Sonda blanda de aspiración", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Riñón", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Pato orinal", descripcion="", cantidad=1))
materiales.append(Material.objects.create(nombre="Cómodo", descripcion="", cantidad=1))

# Materiales de botiquín
#
# materiales.append(Material.objects.create(nombre="Termómetro oral", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Termómetro rectal", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Termómetro digital", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Glucómetro", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Pulsoxímetro", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Cloruro de etilo", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Cinta blanca", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Cinta micropor", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Salbutamol aerosol", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Ligadura", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Caja de punzos", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Electrolitos orales", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Cánulas orofaríngeas", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Cánulas nasofaríngeas", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Conector para oxigeno", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Alcohol", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Jabón quirúrgico", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Cloruro de benzalconio", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Yodopolividina", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Masc.Neonato", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Masc. Pediátrico", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Masc. Adulto", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Puntas nasales pediátrico", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="puntas nasales adulto", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Collarin adulto", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="collarin pediátrico", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Pulsoximetro", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Desfibrilidor automático", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Parche DEA", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Aspirador", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Mascarilla simple neonato", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Mascarilla simple pediátrico", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Mascarilla simple adulto", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Bolsa válvula mascarilla neonato 250 ml", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Bolsa válvula mascarilla lactante 500 ml", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Bolsa válvula mascarilla pediátrica 750 ml", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Bolsa válvula mascarilla adulto 1000 ml", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Esfigmomanómetro pediátrico", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Esfigmomanómetro adulto", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Equipo herramientas de mano", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Equipo básico de sañalización", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Neumático de refacción", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Llave de cruz", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Gato", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Juego de cables pasa-corriente", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Extintor", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Lámpara portátil de emergencia", descripcion="", cantidad=1))
# materiales.append(Material.objects.create(nombre="Mapa", descripcion="", cantidad=1))

fecha = timezone.now()

nombres = ['Azul 1', 'Azul 2', 'Azul 3', 'Azul 4']

for nombre in nombres:
    inventario = Inventario.objects.create(nombre="inventario "+nombre)
    ambulancia = Ambulancia.objects.create(nombre=nombre, inventario=inventario, estado=Ambulancia.activa)
    revision = Revision.objects.create(fecha=fecha)
    revision_ambulancia = RevisionAmbulancia.objects.create(
        fecha=fecha,
        ambulancia=ambulancia,
        gasolina=90,
        liquido_frenos=40
    )
    for material in materiales:
        InventarioMaterial.objects.create(
            inventario=inventario,
            material=material,
            cantidad=material.cantidad,
            revision=revision
        )
Activables.objects.create(cantidad=2)

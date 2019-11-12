from django.shortcuts import render
from ambulancia.models import Ambulancia
from revision.models import Revision, RevisionAmbulancia
from inventario.models import InventarioMaterial
from inventario.models import Inventario
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.db.models import Sum

##### CONTROLLER US09 #####


@login_required
def ver_revisiones(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    inventario = ambulancia.inventario
    ambulancia = Ambulancia.objects.get(inventario=inventario)
    revisiones = Revision.objects.filter(inventario=inventario.id)
    context = {'revisiones': revisiones, 'ambulancia':ambulancia}
    return render(request, '../templates/revision/ver_revisiones.html', context)
##### CONTROLLER US09 #####


@login_required
#### CONTROLLER US42 ######
def ver_detalle_revsion(request, id, id_revision):
    revision = Revision.objects.get(id=id_revision)
    fecha_revision = revision.fecha
    ambulancia = Ambulancia.objects.get(id=id)
    inventario = ambulancia.inventario
    ano_revsion = fecha_revision.year
    mes_revision = fecha_revision.month
    dia_revision = fecha_revision.day
    hora_revision = fecha_revision.hour
    minutos_revision = fecha_revision.minute
    materiales = InventarioMaterial.objects.filter(inventario=inventario, fecha__contains=str(ano_revsion) +'-'+ str(mes_revision) +"-"+ str(dia_revision) +" "+ str(hora_revision)+":"+str(minutos_revision))


    context={'materiales':materiales,'ambulancia':ambulancia,'fecha':fecha_revision}

    return render(request, '../templates/revision/ver_detalle_revision.html', context)
#### CONTROLLER US42 ######

#### CONTROLLER US29 ######

@login_required
def ver_revisiones_ambulancia(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    inventario = ambulancia.inventario
    ambulancia = Ambulancia.objects.get(inventario=inventario)
    revisiones = RevisionAmbulancia.objects.filter(inventario=inventario.id)
    context = {'revisiones': revisiones, 'ambulancia':ambulancia}
    return render(request, '../templates/revision/ver_revisiones_ambulancia.html', context)
#### CONTROLLER US29 ######

#### CONTROLLER US30 ######
@login_required
def ver_detalle_ambulancia(request, id, id_revision):
    revision = Revision.objects.get(id=id_revision)
    ambulancia = Ambulancia.objects.get(id=id)
    context = {
        'revision': revision,
        'ambulancia': ambulancia,
    }
    return render(request, '../templates/revision/ver_detalle_ambulancia.html', context)



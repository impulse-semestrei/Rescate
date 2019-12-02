from django.shortcuts import render
from django.template.defaultfilters import register
from ambulancia.models import Ambulancia
from revision.models import Revision, RevisionAmbulancia
from inventario.models import InventarioMaterial, Inventario
from django.contrib.auth.decorators import login_required
from django import template
from users.decorators import voluntario_required,administrador_required,adminplus_required
from django.utils.decorators import method_decorator
# Create your views here.
from django.db.models import Sum, F, Func
from django.db.models import Q


##### CONTROLLER US09 #####


@administrador_required
def ver_revisiones(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    registros = InventarioMaterial.objects.filter(
        Q(inventario=ambulancia.inventario) | Q(inventario=ambulancia.botiquin) | Q(inventario=ambulancia.monitor)
    ).distinct('revision')
    context = {'registros': registros, 'ambulancia': ambulancia}
    return render(request, '../templates/revision/ver_revisiones.html', context)
##### CONTROLLER US09 #####


@administrador_required
#### CONTROLLER US42 ######
def ver_detalle_revsion(request, id, id_revision):

    ambulancia = Ambulancia.objects.get(id=id)
    materiales = InventarioMaterial.objects.filter(revision=id_revision)
    revision = Revision.objects.get(id=id_revision)


    context={'materiales':materiales,'ambulancia':ambulancia, 'revision': revision}

    return render(request, '../templates/revision/ver_detalle_revision.html', context)
#### CONTROLLER US42 ######

#### CONTROLLER US29 ######

@administrador_required
def ver_revisiones_ambulancia(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    revisiones = RevisionAmbulancia.objects.filter(ambulancia=ambulancia)
    context = {'revisiones': revisiones, 'ambulancia':ambulancia}
    return render(request, '../templates/revision/ver_revisiones_ambulancia.html', context)
#### CONTROLLER US29 ######

#### CONTROLLER US30 ######
@administrador_required
def ver_detalle_ambulancia(request, id, id_revision):
    revision = RevisionAmbulancia.objects.get(id=id_revision)
    ambulancia = Ambulancia.objects.get(id=id)
    context = {
        'revision': revision,
        'ambulancia': ambulancia,
    }
    return render(request, '../templates/revision/ver_detalle_ambulancia.html', context)

#### CONTROLLER US30 ######

def Reportes(request):
    ambulancias = Ambulancia.objects.all()
    materiales = []
    unidad = []
    for ambulancia in ambulancias.iterator():
        ambu = Ambulancia.objects.get(id=ambulancia.id)
        unidad.append(Ambulancia.objects.get(id=ambulancia.id))
        materialesInventario = InventarioMaterial.objects.filter(
            Q(inventario=ambu.inventario) | Q(inventario=ambu.botiquin) | Q(inventario=ambu.monitor)
        ).distinct('revision').order_by('-revision__id').first()
        revision = materialesInventario.revision
        materiales.append(InventarioMaterial.objects.filter(revision=revision))
    objetos=[{}]
    info=[{}]
    for i in materiales:
        info.append(i)

    for i in unidad:
        objetos.append(i)

    fusion = zip(info, objetos)
    print(fusion)

    context={'info':fusion}


    return render(request,'../templates/revision/reportes.html', context)


@register.filter(name = 'substract')
def subtract(value, arg):

    return abs(value - arg)
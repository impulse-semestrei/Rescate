from django.shortcuts import render, redirect
from .models import Ambulancia, Viaje, MaterialUsado
from .forms import CrearAmbulancia
from .forms import CrearAmbulancia, CambiarEstado
from .models import Ambulancia, Viaje, Activables
from inventario.models import Inventario
from django.db import DatabaseError, transaction
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from inventario.models import Inventario
from django.views.generic.edit import UpdateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from revision.models import RevisionAmbulancia
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max
from django.contrib.auth import get_user_model


from django.urls import reverse
import json

from users.decorators import voluntario_required,administrador_required,adminplus_required
from django.utils.decorators import method_decorator

STATUS_SAVED = 'SAVED'
STATUS_ERROR = 'ERROR'
STATUS_UPDATED = 'UPDATED'


# Create your views here.
####### CONTROLLER US44############


@administrador_required
def crear_ambulancia(request):
    if request.method == 'POST':
        form = CrearAmbulancia(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            try:
                new_ambulancia = Ambulancia(
                    nombre=form.cleaned_data.get('nombre'),
                    inventario=form.cleaned_data.get('inventario'),
                )
                new_ambulancia.save()
                context['status'] = STATUS_SAVED
                context['ambulancia_name'] = new_ambulancia.nombre
                return render(request, '../templates/ambulancia/crear_ambulancia.html', context)
            except DatabaseError:
                context['status'] = STATUS_ERROR
                print('ERROR')
                form = CrearAmbulancia()
                return render(request, '../templates/ambulancia/crear_ambulancia.html', context)
    else:
        form = CrearAmbulancia()
    context = {
        'form': form,
    }

    return render(request, '../templates/ambulancia/crear_ambulancia.html', context)


####### CONTROLLER US44############


# -------- CONTROLLER US46 ---------
@voluntario_required
def ver_ambulancias(request):
    ambulancias = Ambulancia.objects.all().order_by('id')
    context = {'Ambulancias': ambulancias,
               'form': CrearAmbulancia(),
               }
    return render(request, '../templates/ambulancia/ver_ambulancia.html', context)


# -------- CONTROLLER US46 ---------


# -------- CONTROLLER US47 ---------
@administrador_required
def eliminar_ambulancias(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    ambulancia.delete()
    #pk = ambulancia.inventario
    #inventario = Inventario.objects.get(id=pk.id)
    #inventario.delete()
    # inventario.fechaMod = timezone.now()
    return redirect('/ambulancia/ver/')


# -------- CONTROLLER US46 ---------

####### CONTROLLER US45############
@administrador_required
def editar_ambulancia(request, pk):
    estado = 'get'
    ambulancia = Ambulancia.objects.get(id=pk)
    form = CrearAmbulancia(request.POST or None, instance=ambulancia)
    if request.method == 'POST' and form.is_valid():
        form.save()
        estado = 'guardado'
    context = {
        'form': form,
        'estado': estado
    }
    return render(request, '../templates/ambulancia/editar_ambulancia.html', context)

####### CONTROLLER US45############



##### CONTROLLER US28 ####
def serializar_ambulancia(ambulancia):
    revision = RevisionAmbulancia.objects.filter(ambulancia=ambulancia)\
                        .order_by('-fecha').first()
    json = {
        'materiales': [
            {
                'nombre': 'Gasolina',
                'id': 1,
                'objetivo': ambulancia.objetivo_gasolina,
                'cantidad': revision.gasolina,
                'medida': 'Porcentaje',
            },
            {
                'nombre': 'Kilometraje',
                'id': 2,
                'objetivo': ambulancia.objetivo_kilometraje,
                'cantidad': revision.kilometraje,
                'medida': 'Kilómetros',
            },
            {
                'nombre': 'Líquido de frenos',
                'id': 3,
                'objetivo': ambulancia.objetivo_liquido_frenos,
                'cantidad': revision.liquido_frenos,
                'medida': 'Porcentaje',
            },
            {
                'nombre': 'Aceite de motor',
                'id': 4,
                'objetivo': ambulancia.objetivo_aceite_motor,
                'cantidad': revision.aceite_motor,
                'medida': 'Porcentaje',
            },
            {
                'nombre': 'Aceite de dirección',
                'id': 5,
                'objetivo': ambulancia.objetivo_aceite_direccion,
                'cantidad': revision.aceite_direccion,
                'medida': 'Porcentaje',
            },
            {
                'nombre': 'Anticongelante',
                'id': 6,
                'objetivo': ambulancia.objetivo_anticongelante,
                'cantidad': revision.anticongelante,
                'medida': 'Porcentaje',
            },
            {
                'nombre': 'Líquido limpiaparabrisas',
                'id': 7,
                'objetivo': ambulancia.objetivo_liquido_limpiaparabrisas,
                'cantidad': revision.liquido_limpiaparabrisas,
                'medida': 'Porcentaje',
            }
        ]
    }
    return json


def guardar_ambulancia(ambulancia, request):
    datos = json.loads(request.body)
    try:
        usuario = get_user_model().objects.get(email=datos["email_paramedico"])
        if not (usuario.is_voluntario or usuario.is_administrador or usuario.is_adminplus):
            return False
    except ObjectDoesNotExist:
        return False

    cantidades = {}
    listo = True
    for item in datos["materiales"]:
        cantidades[item["nombre"]] = item["cantidad"]
        if item["cantidad"] < item["objetivo"]:
            listo = False
    with transaction.atomic():
        try:
            RevisionAmbulancia.objects.create(
                usuario=usuario,
                fecha=timezone.now(),
                ambulancia=ambulancia,
                gasolina=cantidades["Gasolina"],
                kilometraje=cantidades["Kilometraje"],
                liquido_frenos=cantidades["Líquido de frenos"],
                aceite_motor=cantidades["Aceite de motor"],
                aceite_direccion=cantidades["Aceite de dirección"],
                anticongelante=cantidades["Anticongelante"],
                liquido_limpiaparabrisas=cantidades["Líquido limpiaparabrisas"],
                observaciones=datos["observaciones"]
            )
            ambulancia.ambulancia_lista = listo
            ambulancia.save()
        except Exception:
            return False

    return True

@csrf_exempt
def checklist_ambulancia(request, pk):
    ambulancia = Ambulancia.objects.get(id=pk)
    if request.method == "GET":
        return JsonResponse(serializar_ambulancia(ambulancia), safe=False)
    elif request.method == "POST":
        if guardar_ambulancia(ambulancia, request):
            return JsonResponse({"status": "OK"}, safe=False)
        return JsonResponse({"status": "ERROR"}, safe=False)

@csrf_exempt
def lista_ambulancias(request):
    activas = Ambulancia.objects.filter(estado=Ambulancia.activa)
    revisadas = activas.filter(ambulancia_lista=True, inventario_listo=True)
    try:
        num_activables = Activables.objects.order_by('-fecha').first().cantidad
    except AttributeError:
        num_activables = 0
    if activas.count() > 0 and activas.count() - revisadas.count() < num_activables:
        antigua = revisadas\
            .annotate(fecha=Max('inventario__inventariomaterial__revision__fecha'))\
            .order_by('fecha')\
            .first()
        antigua.ambulancia_lista = False
        antigua.inventario_listo = False
        antigua.save()
    output = {'ambulancias': []}
    for ambulancia in activas:
        output['ambulancias'].append(
            {
                'nombre': ambulancia.nombre,
                'id': ambulancia.id,
                'idInventario': ambulancia.inventario_id,
                'inventarioListo': ambulancia.inventario_listo,
                'ambulanciaLista': ambulancia.ambulancia_lista,
            }
        )
    return JsonResponse(output)
##### CONTROLLER US28 ####


####### CONTROLLER US25 ###########
@voluntario_required
def viajes_ambulancia(request, id):
    historial = Viaje.objects.filter(ambulancia_id=id)
    context = {'historial': historial,
               }
    return render(request, '../templates/ambulancia/ver_historial.html', context)
####### CONTROLLER US45############


####### CONTROLLER US25 ###########

######## CONTROLLER US22 ########
@voluntario_required
def materiales_usados(request, id):
    material = MaterialUsado.objects.filter(viaje_id=id)
    viaje = Viaje.objects.get(id=id)
    ambulancia = viaje.ambulancia

    context = {'material': material,
               'viaje': ambulancia,
               }
    return render(request, '../templates/ambulancia/ver_material_usado.html', context)

######## CONTROLLER US22 ########

####### CONTROLLER US26############
@voluntario_required
def ver_control_ambulancias(request):
    context = {
        'ambulancias': Ambulancia.objects.all().order_by('id'),
        'form': CambiarEstado,
    }
    if request.method == 'POST' and (request.user.is_administrador or request.user.is_adminplus):
        # post request
        try:
            Activables.objects.create(cantidad=request.POST['activables'], fecha=timezone.now())
            context['estado'] = 'guardado'
        except DatabaseError:
            context['estado'] = 'error'
    try:
        context['activables'] = Activables.objects.order_by('-fecha').first().cantidad
    except AttributeError:
        context['activables'] = 0
    return render(request, '../templates/ambulancia/control_ambulancias.html', context)

@administrador_required
def control_ambulancias(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    form = CambiarEstado(request.POST)
    if form.is_valid():
        estados = request.POST.get('estado')
        print(estados)
        ambulancia.estado= estados
        ambulancia.save()
        print(ambulancia.estado)
        print('llega')
    return redirect ('ambulancia:ver_control_ambulancias')
####### CONTROLLER US26 ###########


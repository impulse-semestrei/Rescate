from django.shortcuts import render, redirect
from .models import Ambulancia, Viaje, MaterialUsado
from .forms import CrearAmbulancia
from .forms import CrearAmbulancia, CambiarEstado
from .models import Ambulancia, Viaje
from inventario.models import Inventario
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from inventario.models import Inventario
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from revision.models import RevisionAmbulancia
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
@method_decorator(administrador_required, name='dispatch')
class EditarAmbulancia(UpdateView):
    model = Ambulancia
    form_class = CrearAmbulancia
    template_name = 'ambulancia/editar_ambulancia.html'
    success_url = '/ambulancia/ver/'
####### CONTROLLER US45############


##### CONTROLLER US28 ####
def serializar_ambulancia(ambulancia):
    revision = RevisionAmbulancia.objects.filter(ambulancia=ambulancia)\
                        .order_by('-fecha').first()
    json = {
        'materiales': [
            {
                'nombre': 'gasolina',
                'id': 1,
                'objetivo': ambulancia.objetivo_gasolina,
                'cantidad': revision.gasolina,
            },
            {
                'nombre': 'liquido de frenos',
                'id': 2,
                'objetivo': ambulancia.objetivo_liquido_frenos,
                'cantidad': revision.liquido_frenos,
            }
        ]
    }
    return json


def guardar_ambulancia(ambulancia, request):
    datos = json.loads(request.body)
    try:
        cantidades = {}

        for item in datos["materiales"]:
            cantidades[item["nombre"]] = item["cantidad"]

        RevisionAmbulancia.objects.create(
            nombre_paramedico=datos["nombre_paramedico"],
            email_paramedico=datos["email_paramedico"],
            fecha=timezone.now(),
            ambulancia=ambulancia,
            gasolina=cantidades["gasolina"],
            liquido_frenos=cantidades["liquido de frenos"],
            observaciones=datos["observaciones"]
        )
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
    output = {'ambulancias': []}
    for ambulancia in Ambulancia.objects.all():
        output['ambulancias'].append(
            {
                'nombre': ambulancia.nombre,
                'id': ambulancia.id,
                'idInventario': ambulancia.inventario_id
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
    ambulancias = Ambulancia.objects.all().order_by('id')


    context = {
        'ambulancias': ambulancias,
        'form': CambiarEstado,
    }
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

    messages.info(request, 'Se ha cambiado el estado de la ambulancia!')
    return redirect ('ambulancia:ver_control_ambulancias')
####### CONTROLLER US26 ###########


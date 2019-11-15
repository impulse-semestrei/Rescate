from django.shortcuts import render, redirect
from .models import Ambulancia
from .forms import CrearAmbulancia
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

STATUS_CREATED = 'SAVED'
STATUS_ERROR = 'ERROR'
STATUS_UPDATED = 'UPDATED'


# Create your views here.
####### CONTROLLER US44############


@login_required
def crear_ambulancia(request):
    if request.method == 'POST':
        form = CrearAmbulancia(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            try:

                ambulancia = form.cleaned_data.get('nombre')
                inventario = form.cleaned_data.get('inventario')
                Ambulancia.objects.create(nombre=ambulancia, inventario=inventario)
                context['status'] = STATUS_CREATED
                context['ambulancia_nombre'] = ambulancia

                return redirect('ambulancia:ver_ambulancias')
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
@login_required
def ver_ambulancias(request):
    ambulancias = Ambulancia.objects.filter(status=True)
    context = {'Ambulancias': ambulancias,
               'form': CrearAmbulancia
               }
    return render(request, '../templates/ambulancia/ver_ambulancia.html', context)


# -------- CONTROLLER US46 ---------


# -------- CONTROLLER US47 ---------
@login_required
def eliminar_ambulancias(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    ambulancia.status = False
    ambulancia.fecha_mod = timezone.now()
    ambulancia.save()
    pk = ambulancia.inventario
    inventario = Inventario.objects.get(id=pk.id)
    inventario.status = False
    # inventario.fechaMod = timezone.now()
    inventario.save()

    return redirect('/ambulancia/ver/')


# -------- CONTROLLER US46 ---------

####### CONTROLLER US45############


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
        'gasolina': revision.gasolina,
        'liquido_frenos': revision.liquido_frenos
    }
    return json


def guardar_ambulancia(ambulancia, request):
    datos = json.loads(request.body)

    try:
        RevisionAmbulancia.objects.create(
            nombre_paramedico=datos["nombre_paramedico"],
            email_paramedico=datos["email_paramedico"],
            fecha=datos["fecha"],
            ambulancia=ambulancia,
            gasolina=datos["gasolina"],
            liquido_frenos=datos["liquido_frenos"],
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

##### CONTROLLER US28 ####
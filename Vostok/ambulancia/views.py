from django.shortcuts import render, redirect
from .models import Ambulancia
from .forms import CrearAmbulancia
from inventario.models import Inventario
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from inventario.models import Inventario
from django.contrib import messages

STATUS_CREATED = 'SAVED'
STATUS_ERROR = 'ERROR'
STATUS_UPDATED = 'UPDATED'


# Create your views here.
####### CONTROLLER US44############


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
def ver_ambulancias(request):
    ambulancias = Ambulancia.objects.filter(status=True)
    context = {'Ambulancias': ambulancias,
               'form': CrearAmbulancia
               }
    return render(request, '../templates/ambulancia/ver_ambulancia.html', context)


# -------- CONTROLLER US46 ---------


# -------- CONTROLLER US47 ---------
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

def mostrar_editar(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    form = CrearAmbulancia({'nombre': ambulancia.nombre, 'inventario': ambulancia.inventario})
    context = {
        'form': form,
        'ambulancia': ambulancia,
    }
    return render(request, '../templates/ambulancia/editar_ambulancia.html', context)


def editar_ambulancias(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    form = CrearAmbulancia(request.POST)
    if (form.is_valid):
        ambulancia.nombre = request.POST.get('nombre')
        ambulancia.inventario_id = request.POST.get('inventario')
        ambulancia.save()

    ambulancias = Ambulancia.objects.filter(status=True)
    context = {
        'Ambulancias': ambulancias,
        'form': CrearAmbulancia(),
    }
    messages.info(request, 'Se ha guardado exitosamente el cambio')
    return render(request, '../templates/ambulancia/ver_ambulancia.html', context)

####### CONTROLLER US45############

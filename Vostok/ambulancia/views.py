from django.shortcuts import render, redirect
from .forms import CrearAmbulancia, CambiarEstado
from .models import Ambulancia, Viaje
from inventario.models import Inventario
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from inventario.models import Inventario
from django.contrib import messages
from django.views.generic.edit import UpdateView

STATUS_SAVED = 'SAVED'
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
@login_required
def ver_ambulancias(request):
    ambulancias = Ambulancia.objects.all().order_by('id')
    context = {'Ambulancias': ambulancias,
               'form': CrearAmbulancia(),
               }
    return render(request, '../templates/ambulancia/ver_ambulancia.html', context)


# -------- CONTROLLER US46 ---------


# -------- CONTROLLER US47 ---------
@login_required
def eliminar_ambulancias(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    pk = ambulancia.inventario
    inventario = Inventario.objects.get(id=pk.id)
    inventario.delete()
    # inventario.fechaMod = timezone.now()
    return redirect('/ambulancia/ver/')


# -------- CONTROLLER US46 ---------

####### CONTROLLER US45############


class EditarAmbulancia(UpdateView):
    model = Ambulancia
    form_class = CrearAmbulancia
    template_name = 'ambulancia/editar_ambulancia.html'
    success_url = '/ambulancia/ver/'

####### CONTROLLER US45############

####### CONTROLLER US25 ###########
@login_required
def viajes_ambulancia(request, id):
    historial = Viaje.objects.filter(ambulancia_id=id)
    context = {'historial': historial,
               }
    return render(request, '../templates/ambulancia/ver_historial.html', context)
####### CONTROLLER US45############

####### CONTROLLER US26############
def ver_control_ambulancias(request):
    ambulancias = Ambulancia.objects.all().order_by('id')


    context = {
        'ambulancias': ambulancias,
        'form': CambiarEstado,
    }
    return render(request, '../templates/ambulancia/control_ambulancias.html', context)

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

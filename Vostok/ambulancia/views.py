from django.shortcuts import render
from .models import Ambulancia
from .forms import CrearAmbulancia
from inventario.models import Inventario
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required


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
def ver_ambulancias(request):
    ambulancias = Ambulancia.objects.filter(status=True)
    context = {'Ambulancias':ambulancias}
    return render(request, '../templates/ambulancia/ver_ambulancia.html', context)
# -------- CONTROLLER US46 ---------

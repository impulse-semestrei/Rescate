from django.shortcuts import render
from .forms import crearInventarioForm
from .models import Inventario
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from .models import Inventario_Material
from django.utils import timezone


# Create your views here.
####### CONTROLLER US04############

@login_required
def crearInventarioView(request):
    form = crearInventarioForm(request.POST)
    if form.is_valid():

        try:
            temp_form = form.save(commit=False)
            temp_form.save()

            return render(request,'../templates/index.html')
        except DatabaseError:
            return render(request, '../templates/data_base_error.html')
    context = {'form': form}

    return render(request, '../templates/inventario/crear_inventario.html', context)

####### CONTROLLER US04############


####### CONTROLLER US07############
def ver_inventario(request):
    inventarios = Inventario.objects.filter(status=True)
    context = {'inventarios': inventarios, }
    return render(request, '../templates/inventario/ver_inventario.html', context)

####### CONTROLLER US07############

###### CONTROLLER US03 #######


def delete_inventario(request,id):
    inventario = Inventario.objects.get(id=id)
    inventario.status = False
    inventario.fechaMod = timezone.now()
    inventario.save()
    inventarios = Inventario.objects.filter(status=True)
    context = {'inventarios': inventarios, }
    return render(request, '../templates/inventario/ver_inventario.html',context)

###### CONTROLLER US03 #######



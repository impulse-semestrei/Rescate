from django.shortcuts import render
from .forms import crearInventarioForm, AgregarMaterialInventario
from .models import Inventario
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from .models import InventarioMaterial
from material.models import Material


STATUS_SAVED = 'SAVED'
STATUS_ERROR = 'ERROR'
STATUS_NOT_NEW = 'NOT_NEW'


# Create your views here.
####### VIEWS US-04############

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

####### MODELS US-04############


######## CONTROLLER US1 ########


def agregar_material_inventario(request, pk):
    if request.method == 'POST':
        form = AgregarMaterialInventario(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            try:
                inventario = Inventario.objects.get(id=pk)
                material = form.cleaned_data.get('material')
                cantidad = form.cleaned_data.get('cantidad')
                try:
                    inventario_material = InventarioMaterial.objects.get(inventario=inventario, material=material)
                    inventario_material.cantidad = cantidad
                    inventario_material.save()
                except:
                    InventarioMaterial.objects.create(inventario=inventario, material=material, cantidad=cantidad)
                context['status'] = STATUS_SAVED
                return render(request, '../templates/index.html', context)
            except DatabaseError:
                context['status'] = STATUS_ERROR
                form = AgregarMaterialInventario()
                return render(request, '../templates/material/crear_material.html', context)
    else:
        form = AgregarMaterialInventario()
    context = {
        'form': form,
    }
    return render(request, '../templates/material/crear_material.html', context)


######## CONTROLLER US1 ########


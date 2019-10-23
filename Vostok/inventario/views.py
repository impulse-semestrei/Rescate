from django.shortcuts import render, get_object_or_404, redirect
from .forms import crearInventarioForm, AgregarMaterialInventario, EditarMaterialInventario
from .models import Inventario
from django.db import DatabaseError, transaction
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import InventarioMaterial
from django.core.exceptions import ObjectDoesNotExist
from material.models import Material
from django.contrib import messages


STATUS_CREATED = 'CREATED'
STATUS_ERROR = 'ERROR'
STATUS_UPDATED = 'UPDATED'


# Create your views here.
####### CONTROLLER US04############

@login_required
def crearInventarioView(request):
    form = crearInventarioForm(request.POST)
    if form.is_valid():

        try:
            temp_form = form.save(commit=False)
            temp_form.save()

            return render(request, '../templates/index.html')
        except DatabaseError:
            return render(request, '../templates/data_base_error.html')
    context = {'form': form}

    return render(request, '../templates/inventario/crear_inventario.html', context)

####### CONTROLLER US04############


######## CONTROLLER US1 ########

@login_required
def agregar_material_inventario(request, pk):
    inventario = Inventario.objects.get(id=pk)
    context = {
        'nombre_inventario': inventario,
        'id_inventario': inventario.id,
        'lista_materiales': Material.objects.all()
    }
    if request.method == 'POST':
        form = AgregarMaterialInventario(request.POST)
        context['form'] = form
        if form.is_valid():
            try:
                material = form.cleaned_data.get('material')
                cantidad = form.cleaned_data.get('cantidad')
                context['nombre_material'] = material
                context['cantidad'] = cantidad
                try:
                    with transaction.atomic():
                        inventario_material = InventarioMaterial.objects.get(inventario=inventario, material=material)
                        inventario_material.cantidad += cantidad
                        inventario_material.save()
                        context['status'] = STATUS_UPDATED
                except ObjectDoesNotExist:
                    InventarioMaterial.objects.create(inventario=inventario, material=material, cantidad=cantidad)
                    context['status'] = STATUS_CREATED
                return render(request, '../templates/inventario/agregar_material_inventario.html', context)
            except DatabaseError:
                context['status'] = STATUS_ERROR
                return render(request, '../templates/inventario/agregar_material_inventario.html', context)
    else:
        form = AgregarMaterialInventario()
    context['form'] = form
    return render(request, '../templates/inventario/agregar_material_inventario.html', context)


######## CONTROLLER US1 ########

####### CONTROLLER US07############
def ver_inventario(request):
    inventarios = Inventario.objects.filter(status=True)
    context = {
                'inventarios': inventarios,
                'form': crearInventarioForm(),
    }
    return render(request, '../templates/inventario/ver_inventario.html', context)

####### CONTROLLER US07############

###### CONTROLLER US06 #######


def delete_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    inventario.status = False
    inventario.fechaMod = timezone.now()
    inventario.save()
    inventarios = Inventario.objects.filter(status=True)

    context = {'inventarios': inventarios,
               'form': crearInventarioForm(),
    }
    return render(request, '../templates/inventario/ver_inventario.html',context)


###### CONTROLLER US06 #######


####### CONTROLLER US-05############
def ver_inventario_material(request, pk):
    InventarioMateriales = InventarioMaterial.objects.filter(inventario=Inventario.objects.get(id=pk))
    context = {'inventarios': InventarioMateriales.all,
               'inventario_pk': pk,
               'form': EditarMaterialInventario,
               }
    return render(request, '../templates/inventario/ver_material_inventario.html', context)

####### CONTROLLER US-05############


###### CONTROLLER US03 ########

def eliminar_material_inventario(request, inventario_id, material_id):
    material = InventarioMaterial.objects.get(id=material_id)
    material.delete()
    InventarioMateriales = InventarioMaterial.objects.filter(inventario=Inventario.objects.get(id=inventario_id))
    context = {'inventarios': InventarioMateriales.all,
               'inventario_id': inventario_id,
               }
    return render(request, '../templates/inventario/ver_material_inventario.html', context)


###### CONTROLLER US03 ########


###### CONTROLLER US08 ########

def editar_inventario(request, id):

    inventario = Inventario.objects.get(id=id)
    form = crearInventarioForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
    else:
        return redirect('/inventario/ver/')
    inventario.nombre = nombre
    inventario.save()

    return redirect('/inventario/ver/')


###### CONTROLLER US08 ########


###### CONTROLLER US02 ########
def editar_material(request, inventario_id, material_id):
    material = InventarioMaterial.objects.get(inventario__id=inventario_id, material__id=material_id)
    form = EditarMaterialInventario(request.POST)
    if form.is_valid():
        cantidad = form.cleaned_data.get('cantidad')
    else:
        return redirect('inventario:material_inventario', pk=inventario_id)
    material.cantidad = cantidad
    material.save()
    id = material.inventario
    messages.info(request, 'Se ha editado la cantidad del material con exito')
    return redirect('inventario:material_inventario', pk=inventario_id)

###### CONTROLLER US02 ########
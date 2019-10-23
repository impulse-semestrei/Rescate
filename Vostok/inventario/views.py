from django.shortcuts import render, get_object_or_404, redirect
from .forms import crearInventarioForm, AgregarMaterialInventario
from .models import Inventario
from django.db import DatabaseError, transaction
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import InventarioMaterial
from django.core.exceptions import ObjectDoesNotExist
from material.models import Material
import json
from django.http import JsonResponse
from revision.models import Revision


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
               'inventario_id': pk,
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


def serializar_inventario(inventario):
    materiales = inventario.materiales.all()
    output = {"materiales": []}
    for material in materiales:
        output["materiales"].append({
            "id": material.id,
            "nombre": material.nombre,
            "cantidad": material.cantidad
        })
    return json.dumps(output)


def guardar_inventario(inventario, datos_json):
    datos = json.loads(datos_json)
    objects = []
    fecha = timezone.now()
    for item in datos['materiales']:
        try:
            m = Material.objects.get(id=item['id'])
        except ObjectDoesNotExist:
            return False
        objects.append(InventarioMaterial(inventario=inventario, material=m, cantidad=item['cantidad'],fecha=fecha))

    try:
        with transaction.atomic():
            for item in objects:
                item.save()
            Revision.objects.create(inventario=inventario, fecha=timezone.now())
    except Exception:
        return False

    return True


def checklist(request, pk):
    inventario = Inventario.objects.get(id=pk)
    if request.method == "GET":
        return JsonResponse(serializar_inventario(inventario), safe=False)
    elif request.method == "POST":
        if guardar_inventario(inventario, request.POST["datos"]):
            return JsonResponse(json.dumps({"status": "OK"}), safe=False)
        return JsonResponse(json.dumps({"status": "ERROR"}), safe=False)


from ambulancia.models import Ambulancia
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from users.models import CustomUser

from .forms import crearInventarioForm, AgregarMaterialInventario, EditarMaterialInventario
from .models import Inventario
from django.db import DatabaseError, transaction, IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import InventarioMaterial
from django.core.exceptions import ObjectDoesNotExist
from material.models import Material
import json
from django.http import JsonResponse, HttpResponse
from revision.models import Revision
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import UpdateView

from users.decorators import voluntario_required,administrador_required,adminplus_required
from django.utils.decorators import method_decorator

STATUS_CREATED = 'CREATED'
STATUS_ERROR = 'ERROR'
STATUS_UPDATED = 'UPDATED'
STATUS_SAVED = 'SAVED'

# Create your views here.
####### CONTROLLER US04############

@administrador_required
def crearInventarioView(request):
    form = crearInventarioForm(request.POST)
    if form.is_valid():

        try:
            temp_form = form.save(commit=False)
            temp_form.save()

            inventarios = Inventario.objects.filter(status=True)
            context = {
                'inventarios': inventarios,
                'form': crearInventarioForm(),
                'status': STATUS_SAVED,
            }
            #messages.info(request, 'Se ha creado el inventario')
            return render(request, '../templates/inventario/crear_inventario.html', context)

        except DatabaseError:
            messages.info(request, 'Ya existe un inventario con ese nombre.')
            return render(request, '../templates/data_base_error.html')
    context = {'form': form}

    return render(request, '../templates/inventario/crear_inventario.html', context)

####### CONTROLLER US04############


######## CONTROLLER US1 ########

@administrador_required
def agregar_material_inventario(request, pk):
    inventario = Inventario.objects.get(id=pk)
    context = {
        'nombre_inventario': inventario.nombre,
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
                #context['cantidad'] = cantidad

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
@voluntario_required
def ver_inventario(request):
    inventarios = Inventario.objects.all().order_by('id')
    context = {
                'inventarios': inventarios,
                'form': crearInventarioForm(),
    }
    return render(request, '../templates/inventario/ver_inventario.html', context)
####### CONTROLLER US07############


###### CONTROLLER US06 #######
@administrador_required
def delete_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    inventario.delete()
    inventarios = Inventario.objects.all()

    context = {'inventarios': inventarios,
               'form': crearInventarioForm(),
    }
    return render(request, '../templates/inventario/ver_inventario.html', context)


###### CONTROLLER US06 #######


####### CONTROLLER US-05############
@voluntario_required
def ver_inventario_material(request, pk):
    inventario = Inventario.objects.get(id=pk)
    try:
        registros = InventarioMaterial.objects.filter(inventario=inventario)
        revision = registros.order_by('-revision__fecha').first().revision
        materiales = registros.filter(revision=revision)

    except AttributeError:
        print("error")
        materiales= None


    context = {'inventarios': materiales,
               'nombre_inventario': inventario.nombre,
               'inventario_pk': pk,
               'form': EditarMaterialInventario,
               }
    return render(request, '../templates/inventario/ver_material_inventario.html', context)

####### CONTROLLER US-05############


###### CONTROLLER US03 ########
@administrador_required
def eliminar_material_inventario(request, inventario_id, material_id):
    material = InventarioMaterial.objects.get(id=material_id)
    material.delete()
    InventarioMateriales = InventarioMaterial.objects.filter(inventario=Inventario.objects.get(id=inventario_id))
    context = {'inventarios': InventarioMateriales.all,
               'inventario_id': inventario_id,
               }
    return redirect('inventario:material_inventario', pk=inventario_id)



###### CONTROLLER US03 ########


# ###### CONTROLLER US08 ########
@method_decorator(administrador_required, name='dispatch')
class EditarInventario(UpdateView):
    model = Inventario
    form_class = crearInventarioForm
    template_name = 'inventario/editar_inventario.html'
    success_url = '/inventario/ver/'

###### CONTROLLER US08 ########

##### CONTROLLER US21 ####
def serializar_inventario(inventario):
    ultima_revision = InventarioMaterial.objects.filter(inventario=inventario)\
                        .order_by('-revision__fecha').first().revision

    registros = InventarioMaterial.objects.filter(revision=ultima_revision, inventario=inventario)
    output = {"materiales": []}

    for registro in registros:
        output["materiales"].append({
            "id": registro.material.id,
            "nombre": registro.material.nombre,
            "cantidad": registro.cantidad,
            "objetivo": registro.material.cantidad ,

        })
    return output


def guardar_inventario(inventario, request):
    datos = json.loads(request.body)
    objects = []
    fecha = timezone.now()
    try:
        usuario = CustomUser.objects.get(email=datos["email_paramedico"])
    except ObjectDoesNotExist:
        return False

    revision = Revision(
        fecha=fecha,
        usuario=usuario,
        observaciones=datos['observaciones']
    )

    try:
        ambulancia = Ambulancia.objects.get(inventario=inventario)
    except ObjectDoesNotExist:
        return False

    with transaction.atomic():
        listo = True
        revision.save()
        for item in datos['materiales']:
            try:
                m = Material.objects.get(id=item['id'])
            except ObjectDoesNotExist:
                return False
            if item['cantidad'] < item['objetivo']:
                listo = False

            objects.append(InventarioMaterial(
                inventario=inventario,
                material=m,
                cantidad=item['cantidad'],
                revision=revision)
            )
        for item in objects:
            item.save()
        ambulancia.inventario_listo = listo
        ambulancia.save()
    return True

@csrf_exempt
def checklist(request, pk):
    inventario = Inventario.objects.get(id=pk)
    if request.method == "GET":
        return JsonResponse(serializar_inventario(inventario), safe=False)
    elif request.method == "POST":
        if guardar_inventario(inventario, request):
            return JsonResponse({"status": "OK"}, safe=False)
        return JsonResponse({"status": "ERROR"}, safe=False)

##### CONTROLLER US21 ####

###### CONTROLLER US02 ########

@administrador_required
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


####### CONTROLLER US07############
@administrador_required
def editar_inventario_view(request, id):
    inventario = Inventario.objects.get(id=id)
    form = crearInventarioForm({'nombre': inventario.nombre})
    context = {
        'inventario': inventario,
        'form': form,
    }
    return render(request, '../templates/inventario/editar_inventario.html', context)


####### CONTROLLER US07############


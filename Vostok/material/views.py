from django.contrib import messages
from django.shortcuts import render, redirect

from inventario.models import InventarioMaterial
from .models import Material
from .forms import CrearMaterial
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.generic.edit import UpdateView

from users.decorators import voluntario_required,administrador_required,adminplus_required
from django.utils.decorators import method_decorator

STATUS_SAVED = 'SAVED'
STATUS_ERROR = 'ERROR'


######## CONTROLLER US36 ########

@administrador_required
def crear_material(request):
    if request.method == 'POST':
        form = CrearMaterial(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            try:
                new_material = Material(
                    nombre=form.cleaned_data.get('nombre'),
                    descripcion=form.cleaned_data.get('descripcion'),
                    cantidad=form.cleaned_data.get('cantidad'),
                )
                new_material.save()
                context['status'] = STATUS_SAVED
                context['material_name'] = new_material.nombre
                return render(request, '../templates/material/crear_material.html', context)
            except DatabaseError:
                context['status'] = STATUS_ERROR
                form = CrearMaterial()
                return render(request, '../templates/material/crear_material.html', context)
    else:
        form = CrearMaterial()
    context = {
        'form': form,
    }
    return render(request, '../templates/material/crear_material.html', context)

######## CONTROLLER US36 ########


######## CONTROLLER US38 ########

@voluntario_required
def ver_material(request):
    materiales = Material.objects.filter(status=True).order_by('id')
    nombre = Material.objects.all()
    context = {'materiales':materiales,
               'form':CrearMaterial(),
               'nombre': nombre,
               }
    return render(request, '../templates/material/ver_material.html', context)


######## CONTROLLER US38 ########

######## CONTROLLER US39 ########
@administrador_required
def delete_material(request, id):
    InventarioMaterial.objects.filter(material_id=id).delete()

    Material.objects.get(id=id).delete()

    materiales = Material.objects.all()
    context = {
        'materiales': materiales,
        'form': CrearMaterial(),
    }
    return render(request, '../templates/material/ver_material.html', context)

######## CONTROLLER US39 ########


# ------------- CONTROLLER US34 --------------
@method_decorator(administrador_required, name='dispatch')
class EditarMaterial(UpdateView):
    model = Material
    form_class = CrearMaterial
    template_name = 'material/editar_material.html'
    success_url = '/material/ver/'

# ------------- CONTROLLER US34 --------------
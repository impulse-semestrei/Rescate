from django.shortcuts import render

from .models import Material
from .forms import CrearMaterial
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from django.utils import timezone

STATUS_SAVED = 'SAVED'
STATUS_ERROR = 'ERROR'


######## CONTROLLER US36 ########

@login_required
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


def ver_material(request):
    materiales = Material.objects.filter(status=True)
    context = {'materiales':materiales,
               'form':CrearMaterial(),
               }
    return render(request, '../templates/material/ver_material.html', context)


######## CONTROLLER US38 ########

######## CONTROLLER US39 ########

def delete_material(request, id):
    material = Material.objects.get(id=id)
    material.status = False
    material.fecha_mod = timezone.now()
    material.save()

    materiales = Material.objects.filter(status=True)
    context = {
        'materiales': materiales,
        'form': CrearMaterial(),
    }
    return render(request, '../templates/material/ver_material.html', context)

######## CONTROLLER US39 ########


# ------------- CONTROLLER US34 --------------
def editar_material(request, id):
    material = Material.objects.get(id=id)
    form = CrearMaterial(request.POST)
    if(form.is_valid):
        material.nombre = request.POST.get('nombre')
        material.descripcion = request.POST.get('descripcion')
        material.cantidad = request.POST.get('cantidad')
        material.fecha_mod = timezone.now()
        material.save()

    materiales = Material.objects.filter(status=True)
    context = {
        'materiales': materiales,
        'form': CrearMaterial(),
    }
    return render(request, '../templates/material/ver_material.html', context)

def editar_material_view(request, id):
    material = Material.objects.get(id=id)
    form = CrearMaterial({'nombre': material.nombre, 'descripcion': material.descripcion, 'cantidad':material.cantidad})
    context = {
            'material': material,
            'form': form,
               }
    return render(request, '../templates/material/editar_material.html', context)

# ------------- CONTROLLER US34 --------------

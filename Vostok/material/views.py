from django.shortcuts import render

from .models import Material
from .forms import CrearMaterial
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required

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
    materiales = Material.objects.all()
    context = {'materiales':materiales,}
    return render(request, '../templates/material/ver_material.html', context)


######## CONTROLLER US38 ########

######## CONTROLLER US39 ########

def delete_material(request, id):
    materiales = Material.objects.all()
    context = {'materiales':materiales,}
    return render(request, '../templates/material/ver_material.html', context)


"""
def delete_inventario(request,id):
    inventario = Inventario.objects.get(id=id)
    inventario.status = False
    inventario.fechaMod = timezone.now()
    inventario.save()
    inventarios = Inventario.objects.filter(status=True)
    context = {'inventarios': inventarios, }
    return render(request, '../templates/inventario/ver_inventario.html',context)
"""

######## CONTROLLER US39 ########



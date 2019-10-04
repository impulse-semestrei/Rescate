from django.shortcuts import render

from .models import Material
from .forms import CrearMaterial
from django.db import DatabaseError

STATUS_SAVED = 'SAVED'
STATUS_ERROR = 'ERROR'


######## US36 ########


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
                    descripcion=form.cleaned_data.get('descripcion')
                )
                new_material.save()
                context['status'] = STATUS_SAVED
                return render(request, '../templates/crear_material.html', context)
            except DatabaseError:
                context['status'] = STATUS_ERROR
                return render(request, '../templates/crear_material.html', context)
    else:
        form = CrearMaterial()
    context = {
        'form': form,
    }
    return render(request, '../templates/crear_material.html', context)


######## US36 ########



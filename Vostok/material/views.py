from django.shortcuts import render

from .models import Material
from .forms import CrearMaterial
from django.db import DatabaseError

def vistaCrearMaterial(request):
    if request.method == 'POST':
        form = CrearMaterial(request.POST)
        if form.is_valid():
            try:
                new_material = Material(
                    nombre=form.cleaned_data.get('nombre'),
                    descripcion=form.cleaned_data.get('descripcion')
                )
                new_material.save()
                return render(request, '../templates/data_base_error.html')
            except DatabaseError:
                return render(request, '../templates/data_base_error.html')
    else:
        form = CrearMaterial()
    hola=True
    context={
        'hola':hola,
        'form' : form,
    }
    return render(request,'../templates/crear_material.html',context)





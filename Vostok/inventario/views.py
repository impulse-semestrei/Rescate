from django.shortcuts import render
from .forms import crearInventarioForm
from .models import Inventario
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from .models import Inventario_Material


# Create your views here.
####### VIEW US-04############

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

####### VIEW US-04############

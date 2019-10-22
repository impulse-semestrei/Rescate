from django.shortcuts import render
from ambulancia.models import Ambulancia
from revision.models import Revision
from django.contrib.auth.decorators import login_required
# Create your views here.

##### CONTROLLER US09 #####


@login_required
def ver_revisiones(request, id):
    ambulancia = Ambulancia.objects.get(id=id)
    inventario = ambulancia.inventario
    revisiones = Revision.objects.filter(inventario=inventario.id)

    context={'revisiones': revisiones}
    return render(request, '../templates/revision/ver_revisiones.html', context)
##### CONTROLLER US09 #####

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth import logout
from .decorators import voluntario_required,administrador_required,adminplus_required
from .models import CustomUser
from .forms import CustomUserUpdateForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import get_user_model

# CONTROLLER US-14 #


def login(request):
    return render(request, '../templates/users/login.html')

# CONTROLLER US-14 #

def logoutUser(request):
    logout(request)
    return render(request,'../templates/users/login.html')


# CONTROLLER US-10 #
@adminplus_required
def ver_usuarios(request):
    User = get_user_model()
    usuarios = User.objects.all()
    context = {
                'usuarios': usuarios,
              }
    return render(request, '../templates/users/ver_usuarios.html', context)

#### CONTROLLER US12 ####
@adminplus_required
def ver_detalle_usuarios(request,id):
    try:
        User = get_user_model()
        usuario = User.objects.get(id=id)

        if request.method == 'POST':
            if request.POST.get('turno') != "0":
                usuario.turno = request.POST.get('turno')

            if request.POST.get('rol') != "0":
                if request.POST.get('rol') == "1":
                    usuario.is_anon = True
                    usuario.is_voluntario = False
                    usuario.is_administrador = False
                    usuario.is_adminplus = False
                if request.POST.get('rol') == "2":
                    usuario.is_anon = False
                    usuario.is_voluntario = True
                    usuario.is_administrador = False
                    usuario.is_adminplus = False
                if request.POST.get('rol') == "3":
                    usuario.is_anon = False
                    usuario.is_voluntario = False
                    usuario.is_administrador = True
                    usuario.is_adminplus = False
                if request.POST.get('rol') == "4":
                    usuario.is_anon = False
                    usuario.is_voluntario = False
                    usuario.is_administrador = False
                    usuario.is_adminplus = True

            usuario.save()
            return HttpResponseRedirect('/users/ver/')

        context = {'usuario': usuario}
        return render(request,'../templates/users/ver_detalle_usuario.html',context)
    except :
        return render(request,'../templates/data_base_error.html') #cambiar esto a pantalla de error
#### CONTROLLER US12 ####

@adminplus_required
def generar_pin(request, pk):
    get_user_model().objects.get(id=pk).generar_pin()
    return redirect(reverse('users:detalle_usuario', args=[pk]))


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer


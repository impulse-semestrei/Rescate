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
def ver_detalle_usuarios(request,id):
    try:
        User = get_user_model()
        usuario = User.objects.get(id=id)

        if request.method == 'POST':

            form = CustomUserUpdateForm(request.POST)

            if form.is_valid():

                usuario.date_of_birth = form.cleaned_data.get('date_of_birth')
                usuario.cellphone = form.cleaned_data.get('cellphone')
                usuario.is_anon = form.cleaned_data.get('is_anon')
                usuario.is_voluntario = form.cleaned_data.get('is_voluntario')
                usuario.is_administrador = form.cleaned_data.get('is_administrador')
                usuario.is_adminplus = form.cleaned_data.get('is_adminplus')
                usuario.save()
                return HttpResponseRedirect('/users/ver/')

        else:
            form = CustomUserUpdateForm()

        context = {'usuario': usuario, 'form': form}
        return render(request,'../templates/users/ver_detalle_usuario.html',context)
    except :
        return render(request,'../templates/data_base_error.html') #cambiar esto a pantalla de error
#### CONTROLLER US12 ####




class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

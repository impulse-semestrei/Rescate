# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth import logout
from .decorators import voluntario_required,administrador_required,adminplus_required

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


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

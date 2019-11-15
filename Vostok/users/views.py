# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth import  logout

# CONTROLLER US-14 #


def login(request):
    return render(request, '../templates/users/login.html')

# CONTROLLER US-14 #

def logoutUser(request):
    logout(request)
    return render(request,'../templates/users/login.html')


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

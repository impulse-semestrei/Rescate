from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer


######## CONTROLLER US-14#######
def index(request):
    if request.user.is_authenticated:
        print('Dentro con google')
        return render(request, '../templates/index.html')
    else:
        return render(request, '../templates/data_base_error.html')

    context = {logged: 'logged'}
    return render(request, '../templates/index.html', context)


def login(request):
    # if request.user.is_authenticated:
    #     logged = True
    #     context={logged:'logged'}
    #     return render(request, '../templates/index.html',context)
    # else:
        return render(request, '../templates/users/login.html')
######## CONTROLLER US-14#######

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer
from django.http import JsonResponse


from google.oauth2 import id_token
from google.auth.transport import requests

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
        return render(request, '..//users/login.html')
######## CONTROLLER US-14#######

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def googleUserIsValid(token):


    # (Receive token by HTTPS POST)
    # ...

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
    except ValueError:
        # Invalid token
        pass

def test(request):
    print(request.GET)

    return JsonResponse({'hola': 'hola'})
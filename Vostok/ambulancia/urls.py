from django.urls import path
from .views import crear_ambulancia


app_name = "ambulancia"

######## CONTROLLER US44 ########
urlpatterns = [
    path('crear/', crear_ambulancia, name='crear'),
]
######## CONTROLLER US44 ########

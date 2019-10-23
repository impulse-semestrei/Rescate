from django.urls import path
from . import views


app_name = "ambulancia"

######## CONTROLLER US44 ########
urlpatterns = [
    path('crear/', views.crear_ambulancia, name='crear'),
    path('ver/', views.ver_ambulancias, name='ver_ambulancias'),
]
######## CONTROLLER US44 ########

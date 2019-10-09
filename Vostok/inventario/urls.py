from django.conf import settings
#from django.contrib.auth.views import logout
from django.urls import path
from django.urls import include
from .views import crearInventarioView, agregar_material_inventario, ver_inventario

app_name = 'inventario'

####### URLS US-04############

urlpatterns = [
    path('crear/', crearInventarioView), ######## URLS US01 ########
    path('<int:pk>/agregar_material/', agregar_material_inventario, name='agregar_material_inventario'),
    path('ver/', ver_inventario, name='ver_inventario')
]

####### URLS US-04############
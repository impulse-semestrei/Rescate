from django.conf import settings
#from django.contrib.auth.views import logout
from django.urls import path
from django.urls import include
from .views import crearInventarioView, agregar_material_inventario


####### URLS US-04############

urlpatterns = [
    path('crear/', crearInventarioView),
    path('<int:pk>/agregar_material/', agregar_material_inventario, name='agregar_material_inventario')

]

####### URLS US-04############
from django.conf import settings
#from django.contrib.auth.views import logout
from django.urls import path
from django.urls import include
<<<<<<< HEAD
from .views import crearInventarioView
from .views import ver_inventario,delete_inventario

####### URLS US-04############
app_name= "inventario"
urlpatterns = [

    path('crear/', crearInventarioView),
    path('ver/',ver_inventario , name='ver_inventario'),
    path('delete/<int:id>/',delete_inventario,name="delete_inventario")
=======
from .views import crearInventarioView, agregar_material_inventario, ver_inventario

app_name = 'inventario'

####### URLS US-04############
>>>>>>> 318f7ba2de846503cfd84d1339d1bd0619a6e2a9

urlpatterns = [
    path('crear/', crearInventarioView), ######## URLS US01 ########
    path('<int:pk>/agregar_material/', agregar_material_inventario, name='agregar_material_inventario'),
    path('ver/', ver_inventario, name='ver_inventario')
]

####### URLS US-04############
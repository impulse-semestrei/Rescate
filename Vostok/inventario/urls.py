from django.conf import settings
#from django.contrib.auth.views import logout
from django.urls import path
from django.urls import include
from .views import crearInventarioView
from .views import ver_inventario,delete_inventario

####### URLS US-04############
app_name= "inventario"
urlpatterns = [

    path('crear/', crearInventarioView),
    path('ver/',ver_inventario , name='ver_inventario'),
    path('delete/<int:id>/',delete_inventario,name="delete_inventario")

]

####### URLS US-04############
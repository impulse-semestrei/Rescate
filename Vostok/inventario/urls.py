from django.urls import path
from .views import crearInventarioView, agregar_material_inventario, ver_inventario, delete_inventario, ver_inventario_material


####### URLS US-04############


app_name= "inventario"
urlpatterns = [
    path('crear/', crearInventarioView),
    path('ver/', ver_inventario, name='ver_inventario'),
    path('<int:pk>/agregar_material/', agregar_material_inventario, name='agregar_material_inventario'),
    path('delete/<int:id>/', delete_inventario,name="delete_inventario"),
    path('<int:pk>/ver/material_inventario', ver_inventario_material, name='material_inventario') ######## URLS US05 ########
]


####### URLS US-04############




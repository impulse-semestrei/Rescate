from django.urls import path
from . import views


app_name = "ambulancia"

######## CONTROLLER US44, US45########
urlpatterns = [
    path('crear/', views.crear_ambulancia, name='crear'),
    path('ver/', views.ver_ambulancias, name='ver_ambulancias'),
    path('editar/<int:id>/', views.editar_ambulancias, name="editar_ambulancias"),
    path('editar_ambulancia/<int:id>/', views.mostrar_editar, name="mostrar_editar"),
    path('eliminar/<int:id>', views.eliminar_ambulancias, name='eliminar_ambulancia'),
    path('ver_control_ambulancias', views.ver_control_ambulancias, name='ver_control_ambulancias'),
    path('control_ambulancias/<int:id>', views.control_ambulancias, name='control_ambulancias'),
]
######## CONTROLLER US44, US45 ########

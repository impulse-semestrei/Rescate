from django.urls import path
from . import views


app_name = "ambulancia"

######## CONTROLLER US44, US45########
urlpatterns = [
    path('crear/', views.crear_ambulancia, name='crear'),
    path('ver/', views.ver_ambulancias, name='ver_ambulancias'),
    path('editar/<int:id>/', views.editar_ambulancias, name="editar_ambulancias"),
    path('eliminar/<int:id>', views.eliminar_ambulancias, name='eliminar_ambulancia'),
]
######## CONTROLLER US44, US45 ########

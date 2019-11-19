from django.urls import path
from . import views


app_name = "ambulancia"

######## CONTROLLER US44, US45########
urlpatterns = [
    path('crear/', views.crear_ambulancia, name='crear'),
    path('ver/', views.ver_ambulancias, name='ver_ambulancias'),
    path('editar/<int:pk>/', views.EditarAmbulancia.as_view(), name="editar_ambulancia"),
    path('eliminar/<int:id>', views.eliminar_ambulancias, name='eliminar_ambulancia'),
    path('<int:pk>/json/', views.checklist_ambulancia, name='checklist_ambulancia'),
    path('ver_control_ambulancias', views.ver_control_ambulancias, name='ver_control_ambulancias'),
    path('control_ambulancias/<int:id>', views.control_ambulancias, name='control_ambulancias'),
    path('viajes/<int:id>', views.viajes_ambulancia, name='viajes_ambulancia'),
    path('json/', views.lista_ambulancias, name='lista_ambulancias')
]
######## CONTROLLER US44, US45 ########

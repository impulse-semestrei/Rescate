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
    path('viajes/<int:id>', views.viajes_ambulancia, name='viajes_ambulancia'),
]
######## CONTROLLER US44, US45 ########

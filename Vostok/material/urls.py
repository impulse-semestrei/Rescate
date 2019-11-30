from django.urls import path
from . import views

app_name = 'material'


urlpatterns = [

    path('crear/', views.crear_material, name='crear'),
    path('ver/', views.ver_material, name='ver_material'),
    path('delete/<int:id>/', views.delete_material, name="delete_material"),
    path('editar/<int:pk>/', views.editar_material, name="editar_material"),
]

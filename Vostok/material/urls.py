from django.urls import path
from .views import crear_material
from .views import ver_material

app_name = 'material'


urlpatterns = [
    path('crear/', crear_material, name='crear'),
    path('ver/', ver_material, name='ver_material'),
]

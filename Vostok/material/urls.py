from django.urls import path
from .views import crear_material

app_name = 'material'


urlpatterns = [
    path('crear/', crear_material, name='crear'), ######## US36 ########
]

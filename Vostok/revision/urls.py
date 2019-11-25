from django.urls import path
from .views import ver_revisiones, ver_detalle_revsion, ver_revisiones_ambulancia, ver_detalle_ambulancia

app_name = 'revision'


urlpatterns = [
    path('<int:id>/revisiones/', ver_revisiones, name='revisiones'),

    ###### URLS US42 #####
    path('<int:id>/revisiones/<int:id_revision>/', ver_detalle_revsion, name='detalle_revision'),
    ###### URLS US42 #####
    path('<int:id>/revisiones_ambulancia/', ver_revisiones_ambulancia, name='revisiones_ambulancia'), ###### URLS US29 #####
    path('<int:id>/estado_ambulancia/<int:id_revision>/', ver_detalle_ambulancia, name='detalle_ambulancia'), ###### URLS US30 #####
]

from django.urls import path
from .views import ver_revisiones, ver_detalle_revsion

app_name = 'revision'


urlpatterns = [
    path('<int:id>/revisiones/', ver_revisiones, name='revisiones'),

    ###### URLS US42 #####
    path('<int:id>/revisiones/<int:id_revision>/', ver_detalle_revsion, name='detalle_revision')
    ###### URLS US42 #####

]

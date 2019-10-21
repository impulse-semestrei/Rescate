from django.urls import path
from .views import ver_revisiones

app_name = 'revision'


urlpatterns = [
    path('<int:id>/revisiones/', ver_revisiones, name='revisiones'),


]

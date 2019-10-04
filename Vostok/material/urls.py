from django.conf import settings
#from django.contrib.auth.views import logout
from django.urls import path
from django.urls import include
from .views import vistaCrearMaterial


urlpatterns = [
    path('crear/',vistaCrearMaterial),

]
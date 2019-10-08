from django.conf import settings
#from django.contrib.auth.views import logout
from django.urls import path
from django.urls import include
from .views import crearInventarioView


####### URLS US-04############
urlpatterns = [
    path('crear/', crearInventarioView),

]

####### URLS US-04############
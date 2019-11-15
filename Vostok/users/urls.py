from django.urls import path
from . import views
from dashboard.views import index

urlpatterns = [
    path('', views.login, name='login'),
    path('index/',index),
    path('logout/',views.logoutUser,name='logout')
]


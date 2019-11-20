from django.urls import path
from . import views
from dashboard.views import index


app_name = 'users'


urlpatterns = [
    path('', views.login, name='login'),
    path('index/', index, name='index'),
    path('logout/',views.logoutUser,name='logout'),
    path('ver/', views.ver_usuarios, name='ver_usuarios')
]


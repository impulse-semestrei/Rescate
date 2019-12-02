from django.urls import path
from . import views
from dashboard.views import index


app_name = 'users'


urlpatterns = [
    path('', views.login, name='login'),
    path('index/', index, name='index'),
    path('logout/',views.logoutUser,name='logout'),
    path('users/ver/', views.ver_usuarios, name='ver_usuarios'),
    path('users/ver/<int:id>', views.ver_detalle_usuarios, name="detalle_usuario"),
    path('users/generar_pin/<int:pk>', views.generar_pin, name="generar_pin"),
]


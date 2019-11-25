"""Vostok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'api', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('material/', include('material.urls')),
    path('inventario/', include('inventario.urls')),
    path('api/', include(router.urls)),
    path('revision/', include('revision.urls')),
    path('ambulancia/', include('ambulancia.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),

]

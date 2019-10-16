from django.conf import settings
#from django.contrib.auth.views import logout
from django.urls import path
from django.urls import include
from users.views import index
from users.views import login
from users.views import login_movil


urlpatterns = [
    path('',login),
    path('auth/google/', include('social_django.urls', namespace='social')),
    path('index/',index),
    path('test', login_movil)
    #path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
    #name='logout'),

]
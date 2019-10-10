from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



######## CONTROLLER US-14#######
def index(request):
    if request.user.is_authenticated:
        print('Dentro con google')
        return render(request, '../templates/index.html')
    else:
        return render(request, '../templates/data_base_error.html')






def login(request):
    return render(request, '../templates/users/login.html')
######## CONTROLLER US-14#######
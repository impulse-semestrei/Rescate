from django.shortcuts import render

# Create your views here.


def index(request):

    if request.user.is_authenticated:
        return render(request, '../templates/dashboard/index.html')
    else:
        return render(request, '../users/templates/users/login.html')

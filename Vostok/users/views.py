from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



def index(request):
        if request.user.is_authenticated:
            print('Dentro con google')
            logged= True
        else:
            print('Nel con google')
            logged=False


        context={logged:'logged'}

        return render(request, '../templates/index.html',context)
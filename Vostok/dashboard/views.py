from django.shortcuts import render
from .forms import CustomForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        try:
            User = get_user_model()
            usuario = User.objects.get(id=request.user.id)

            if request.method == 'POST':
                form = CustomForm(request.POST)
                if form.is_valid():
                    usuario.date_of_birth = form.cleaned_data.get('date_of_birth')
                    usuario.cellphone = form.cleaned_data.get('cellphone')
                    usuario.save()
                    return HttpResponseRedirect('/users/ver/')

            else:
                form = CustomForm()

            context = {'usuario': usuario, 'form': form}
            return render(request, '../templates/dashboard/index.html',context)

        except:
            return render(request, '../templates/data_base_error.html')  # cambiar esto a pantalla de error
    else:
        return render(request, '../users/templates/users/login.html')

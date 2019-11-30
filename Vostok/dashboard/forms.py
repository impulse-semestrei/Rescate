from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from django.contrib.auth import get_user_model

class CustomForm(forms.ModelForm):

    cellphone = forms.CharField(label='Celular', max_length=10, required=True, widget= forms.TextInput
                           (attrs={'placeholder':'10 dígitos: xxx xxx xxxx'}))
    date_of_birth = forms.DateField(label='Fecha de Nacimiento', widget=forms.SelectDateWidget(years=range(1900, 2025)), required=True)

    class Meta:
        User = get_user_model()
        model = User
        fields = ('cellphone','date_of_birth')
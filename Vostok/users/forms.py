from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

### FORM US12 ###

class CustomUserUpdateForm(forms.ModelForm):

    #cellphone = forms.CharField(label='Celular')
    #date_of_birth = forms.DateField(label='Fecha de Nacimiento', widget=forms.SelectDateWidget)

    class Meta:
        User = get_user_model()
        model = User
        fields = ('is_anon', 'is_voluntario', 'is_administrador', 'is_adminplus','turno')

### FORM US12 ###

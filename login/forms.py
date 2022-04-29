from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from login.models import Avatar


class UserRegisterForm(UserCreationForm):
    first_name: forms.CharField()
    last_name: forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        labels = {'username': 'Usuario', 'email':'E-mail','first_name': 'Nombre', 'last_name':'Apellido'}
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm): 
    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}


class AvatarForm(forms.ModelForm):
    class Meta:
        model= Avatar
        fields= ['user', 'imagen']
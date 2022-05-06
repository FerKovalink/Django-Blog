from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from login.forms import UserRegisterForm, UserEditForm


def login_request(request):

      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  user = authenticate(username = usuario , password = contra)
                  
                  if user is not None:
                        login(request, user)
                        return render (request, "base.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        return render (request, "base.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "base.html", {"mensaje":"Formulario erroneo"})

      form = AuthenticationForm()
      return render(request, "login.html", {'form': form})



def register(request):

      
      if request.method == "POST":
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']                 
                  form.save()
                  return render(request, "base.html")
      else: 
            form = UserRegisterForm()

      return render(request, "registro.html", {"form": form})
      
      

'''def showimage(request):

    lastimage= Avatar.objects.last()
    imagefile= lastimage.imagefile
    form= AvatarForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context= {'imagen': imagefile, 'form': form}
    
    return render(request, 'base.html', context) '''



def editarPerfil(request): 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid:
                  informacion = miFormulario.fields
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
                  return render(request, "base.html")

      else:
            miFormulario = UserEditForm(initial={'email':usuario.email})

      return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})




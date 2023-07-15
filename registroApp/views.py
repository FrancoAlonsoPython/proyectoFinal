from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from registroApp.forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "registroApp/login/login.html", {'form': form})
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu')  
        return render(request, "menu.html", {'form': form, 'error': 'Nombre de usuario o contraseña incorrectos'})


def signup(request):
    if request.method == 'GET':
        return render(request, 'registroApp/signup/signup.html', {'form': CustomUserCreationForm()})
    elif request.method == 'POST':
        form = CustomUserCreationForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('registroApp:login')
        else:
            return render(request, 'registroApp/signup/signup.html', {
                'form' : CustomUserCreationForm(),
                "error": "Contraseña incorrecta o usuario existente"
            })
        
@login_required
def perfilview(request):
    user = request.user
    return render(request, 'registroApp/perfil/perfil.html', {'user': user})

def editarPerfil(request):
    return render(request, 'registroApp/perfil/editarPerfil.html')   
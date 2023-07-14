from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

from registroApp.forms import UserRegisterForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(request, username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request , "menu.html")
            else:
                return render(request, "registroApp/login/login.html", {"mensaje": "Error, datos incorrectos"})
        else:
            return render(request, "menu.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, "registroApp/login/login.html", {"form": form})


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registroApp:login')
    else:
        form = UserRegisterForm()

    return render(request, 'registroApp/signup/signup.html', {'form': form})
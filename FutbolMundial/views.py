from django.shortcuts import render
from FutbolMundial.models import Autores, Comentario
from django.shortcuts import render, redirect
from FutbolMundial.forms import  UserEditForm
#from django.contrib.auth import login, logout, authenticate
#from FutbolMundial.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .models import Page
from django.contrib.auth.models import User
from registroApp.models import CustomUser
# Create your views here.

def page_detail(request, pageId):
    page = Page.objects.get(id=pageId)
    return render(request, 'page_detail.html', {'page': page})

def menu(request):
    return render(request, 'menu.html')

def sobreMi(request):
    return render(request, 'sobreMi.html')

def blog(request):
    futbol = Autores.objects.all()
    pages = Page.objects.all()

    if request.method == "POST":
        nombre = request.POST["nombre"]
        mensaje = request.POST["mensaje"]
        obj = Comentario(nombre=nombre, comentario=mensaje)
        obj.save()
        mensaje = "Gracias por tu comentario!"
        return render (request,"blog.html" , {"futbol": futbol, "pages": pages,"mensaje":mensaje})
    return render(request, "blog.html", {"futbol" : futbol ,"pages": pages,})

@login_required
def inicio(request):
    return render(request, "inicio.html")

def contacto(request):
    return render(request, "contacto.html")


#def login_request(request):
#    if request.method == "POST":
#        form = AuthenticationForm(request,data=request.POST)
#
#        if form.is_valid():
#            usuario = form.cleaned_data.get('username')
#            contra = form.cleaned_data.get('password')
#
#            user = authenticate(username=usuario, password=contra)
#
#            if user is not None:
#                login(request,user)
#                return render(request,"inicio.html", {"mensaje": f"Bienvenido {usuario}"})
#            else:
#                return render(request,"inicio.html",{"mensaje": "Error, datos incorrectos"})
#        else:
#                return render(request,"inicio.html",{"mensaje": "Error, formulario incorrecto"}) 
#    form = AuthenticationForm()
#
#    return render(request,"login.html", {"form":form})      

#def register(request):
#    if request.method == "POST":
#        form = UserRegisterForm(request.POST)
#        if form.is_valid():
#
#            username = form.cleaned_data["username"]
#            form.save()
#            return render(request, "inicio.html" , {"mensaje": "Usuario Creado!"})
#        
#    else:
#        form=UserRegisterForm()
#
#    return render (request,"registro.html" , {"form":form})

def LeerAutor(request):

    autores = Autores.objects.all() 

    contexto= {"autores":autores} 

    return render(request, "LeerAutor.html",contexto)

class AutorList(ListView):

    model = Autores
    template_name = "autor_list.html"
    

class AutorDetalle(DetailView):
    model = Autores
    template_name = "autor_detalle.html"

class AutorCreacion(CreateView):
    model = Autores
    template_name = "autor_form.html"
    success_url = "/FutbolMundial/autor/list"
    fields = ["nombre"]

class AutorUpdate(UpdateView):
    model = Autores
    template_name = "autor_form.html"
    success_url = "/FutbolMundial/autor/list"
    fields = ["nombre"]

class AutorDelete(DeleteView):
    model = Autores
    template_name = "autor_confirm_delete.html"
    success_url = "/FutbolMundial/autor/list"

def perfilview(request):
    return render(request, 'perfil/perfil.html')


def editarPerfil(request):
    return render(request, 'perfil/editarPerfil.html')
from django.shortcuts import render
from FutbolMundial.models import Autores, Comentario
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Page
from registroApp.views import *

def page_detail(request, pageId):
    page = Page.objects.get(id=pageId)
    return render(request, 'page_detail.html', {'page': page})

#@login_required
def menu(request):
    return render(request, 'menu.html')

#@login_required
def sobreMi(request):
    return render(request, 'sobreMi.html')

#@login_required
def blog(request):
    futbol = Autores.objects.all()
    pages = Page.objects.all()

    return render(request, "blog.html" ,{"futbol" : futbol ,"pages": pages,})

#@login_required
def inicio(request):
    return render(request, "inicio.html")

#@login_required
def contacto(request):
    futbol = Autores.objects.all()
    pages = Page.objects.all()

    if request.method == "POST":
        nombre = request.POST["nombre"]
        mensaje = request.POST["mensaje"]
        obj = Comentario(nombre=nombre, comentario=mensaje)
        obj.save()
        mensaje = "Gracias por tu comentario!"
        return render (request,"contacto.html" , {"futbol": futbol, "pages": pages,"mensaje":mensaje})
    return render(request, "contacto.html", {"futbol" : futbol ,"pages": pages,})

@login_required
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


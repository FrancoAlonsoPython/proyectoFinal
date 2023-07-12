from django.urls import path 
from FutbolMundial.views import *
from django.contrib.auth import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', login_request),
    path('inicio/', inicio, name = "Inicio"),
    path('blog/' , blog, name = "blog"),
    path('contacto/', contacto, name = "contacto"),
    path('LeerAutor/',LeerAutor, name = "LeerAutor"),
    path('login/', login_request, name="Login"),
    #path('registro/', register, name='Registro'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='Logout'),
    path('<int:pk>', AutorDetalle.as_view(), name='Detail'),
    path('borar/<int:pk>', AutorDelete.as_view(), name='Delete'),
    path('editar/<int:pk>', AutorUpdate.as_view(), name='Edit'),
    path('nuevo/', AutorCreacion.as_view(), name='New'),
    path('menu/', menu, name='menu'),
    path('autor/list/', AutorList.as_view(), name='autor_list'),
    path('sobreMi/', sobreMi, name= "sobreMi"),
    path('pages/<int:pageId>/', page_detail, name='page_detail'),


]
from django.urls import path 
from FutbolMundial.views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('inicio/', inicio, name = "Inicio"),
    path('blog/' , blog, name = "blog"),
    path('contacto/', contacto, name = "contacto"),
    path('LeerAutor/',LeerAutor, name = "LeerAutor"),
    path('logout/', LogoutView.as_view(template_name='registroApp/login/login.html'), name='Logout'),
    path('<int:pk>', AutorDetalle.as_view(), name='Detail'),
    path('borar/<int:pk>', AutorDelete.as_view(), name='Delete'),
    path('editar/<int:pk>', AutorUpdate.as_view(), name='Edit'),
    path('nuevo/', AutorCreacion.as_view(), name='New'),
    path('menu/', menu, name='menu'),
    path('autor/list/', AutorList.as_view(), name='autor_list'),
    path('sobreMi/', sobreMi, name= "sobreMi"),
    path('pages/<int:pageId>/', page_detail, name='page_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registroApp/login/login.html'), name='login'),
    path('perfil/', perfilview, name="perfil"),
    path('perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
] 
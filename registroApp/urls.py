from django.urls import path
from django.contrib.auth.views import LogoutView
from registroApp.views import *
from FutbolMundial.views import inicio
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'registroApp'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(template_name="registroApp/login/login.html"), name="Logout"),
    path('inicio/', inicio, name = "Inicio"),
    path('perfil/', perfilview, name="perfil"),
    path('perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    ]

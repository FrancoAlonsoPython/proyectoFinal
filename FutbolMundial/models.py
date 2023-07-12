from django.db import models
#from django.contrib.auth.models import AbstractUser
#from .models import CustomUser

class Page(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title

#class CustomUser(AbstractUser):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#
#    def __str__(self):
#        return self.username

class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField(max_length=400)
    imagen = models.URLField()
    autor = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    nombre = models.CharField(max_length=60)
    comentario = models.TextField(max_length=400)
    
    def __str__(self):
        return self.nombre
    
class Registro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)


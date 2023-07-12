from django.contrib import admin
from FutbolMundial.models import Autores,Comentario
from django.contrib.admin.models import LogEntry
#from .models import CustomUser
from .models import Registro

#admin.site.register(CustomUser)
admin.site.register(Autores)
admin.site.register(Comentario)
admin.site.register(LogEntry)
admin.site.register(Registro)
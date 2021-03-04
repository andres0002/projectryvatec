from django.contrib import admin
from ProyectoRyvatecApp.models import Usuario
from ProyectoRyvatecApp.models import Dispositivo
from ProyectoRyvatecApp.models import Categoria

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Dispositivo)
admin.site.register(Categoria)

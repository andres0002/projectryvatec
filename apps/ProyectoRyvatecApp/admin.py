from django.contrib import admin
from apps.ProyectoRyvatecApp.models import Usuario
from apps.ProyectoRyvatecApp.models import Dispositivo
from apps.ProyectoRyvatecApp.models import Categoria

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Dispositivo)
admin.site.register(Categoria)

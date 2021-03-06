from django.conf.urls import url
from apps.tecnico.views import PerfilTecnico
from apps.tecnico.views import Home
from apps.tecnico.views import Proveedores
from apps.tecnico.views import Tecnicos
from apps.tecnico.views import QuienesSomos

app_name = 'tecnico'

urlpatterns = [
    url(r'^perfil-tecnico/', PerfilTecnico.as_view(), name='perfil_tecnico'),
    url(r'^home', Home.as_view(), name='home'),
    url(r'^proveedores/', Proveedores.as_view(), name='proveedores'),
    url(r'^tecnicos/', Tecnicos.as_view(), name='tecnicos'),
    url(r'^quienes-somos/', QuienesSomos.as_view(), name='quienes_somos'),
]
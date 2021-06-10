from django.conf.urls import url
from apps.proveedor.views import PerfilProveedor
from apps.proveedor.views import ListarDispositivos
from apps.proveedor.views import AdicionarDispositivo
from apps.proveedor.views import VisualizarDispositivo
from apps.proveedor.views import ModificarDispositivo
from apps.proveedor.views import BorrarDispositivo
from apps.proveedor.views import Home
from apps.proveedor.views import Proveedores
from apps.proveedor.views import Tecnicos
from apps.proveedor.views import QuienesSomos

app_name = 'proveedor'

urlpatterns = [
    url(r'^perfil-proveedor/', PerfilProveedor.as_view(), name='perfil_proveedor'),
    url(r'^listar-dispositivos/', ListarDispositivos.as_view(), name='listar_dispositivos'),
    url(r'^adicionar-dispositivos/', AdicionarDispositivo.as_view(), name='adicionar_dispositivos'),
    url(r'^visualizar-dispositivos/(?P<id_dispositivo>\w+)', VisualizarDispositivo.as_view(), name='visualizar_dispositivos'),
    url(r'^modificar-dispositivos/(?P<id_dispositivo>\w+)', ModificarDispositivo.as_view(), name='modificar_dispositivos'),
    url(r'^borrar-dispositivos/(?P<id_dispositivo>\w+)', BorrarDispositivo.as_view(), name='borrar_dispositivos'),
    url(r'^home', Home.as_view(), name='home'),
    url(r'^proveedores/', Proveedores.as_view(), name='proveedores'),
    url(r'^tecnicos/', Tecnicos.as_view(), name='tecnicos'),
    url(r'^quienes-somos/', QuienesSomos.as_view(), name='quienes_somos'),
]

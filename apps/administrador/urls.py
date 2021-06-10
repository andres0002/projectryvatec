
from django.conf.urls import url
from apps.administrador.views import ListadoUsuarios
from apps.administrador.views import PerfilAdministrador
from apps.administrador.views import AdicionarUsuario
from apps.administrador.views import VisualizarUsuario
from apps.administrador.views import ModificarUsuario
from apps.administrador.views import BorrarUsuario
from apps.administrador.views import ListarCategoria
from apps.administrador.views import AdicionarCategoria
from apps.administrador.views import VisualizarCategoria
from apps.administrador.views import ModificarCategoria
from apps.administrador.views import BorrarCategoria
from apps.administrador.views import Home
from apps.administrador.views import Proveedores
from apps.administrador.views import Tecnicos
from apps.administrador.views import QuienesSomos

app_name = 'administrador'

urlpatterns = [
    url(r'^listar-usuarios/', ListadoUsuarios.as_view(), name='listar_usuarios'),
    url(r'^perfil-administrador/', PerfilAdministrador.as_view(), name='perfil_administrador'),
    url(r'^adicionar-usuarios/', AdicionarUsuario.as_view(), name='adicionar_usuarios'),
    url(r'^visualizar-usuario/(?P<id_usuario>\w+)', VisualizarUsuario.as_view(), name='visualizar_usuario'),
    url(r'^modificar-usuario/(?P<id_usuario>\w+)', ModificarUsuario.as_view(), name='modificar_usuario'),
    url(r'^borrar-usuario/(?P<id_usuario>\w+)', BorrarUsuario.as_view(), name='borrar_usuario'),

    url(r'^listar-categorias/', ListarCategoria.as_view(), name='listar_categoria'),
    url(r'^adicionar-categoria/', AdicionarCategoria.as_view(), name='adicionar_categoria'),
    url(r'^visualizar-categoria/(?P<id_categoria>\w+)', VisualizarCategoria.as_view(), name='visualizar_categoria'),
    url(r'^modificar-categoria/(?P<id_categoria>\w+)', ModificarCategoria.as_view(), name='modificar_categoria'),
    url(r'^borrar-categoria/(?P<id_categoria>\w+)', BorrarCategoria.as_view(), name='borrar_categoria'),

    url(r'^home', Home.as_view(), name='home'),
    url(r'^proveedores/', Proveedores.as_view(), name='proveedores'),
    url(r'^tecnicos/', Tecnicos.as_view(), name='tecnicos'),
    url(r'^quienes-somos/', QuienesSomos.as_view(), name='quienes_somos'),
]

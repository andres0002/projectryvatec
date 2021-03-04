
from django.conf.urls import url
from administrador.views import ListadoUsuarios
from administrador.views import PerfilAdministrador
from administrador.views import AdicionarUsuario
from administrador.views import VisualizarUsuario
from administrador.views import ModificarUsuario
from administrador.views import BorrarUsuario
from administrador.views import ListarCategoria
from administrador.views import AdicionarCategoria
from administrador.views import VisualizarCategoria
from administrador.views import ModificarCategoria
from administrador.views import BorrarCategoria

from administrador.views import Home
from administrador.views import Proveedores
from administrador.views import Tecnicos
from administrador.views import QuienesSomos


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

from cliente.views import PerfilCliente

app_name = 'cliente'

urlpatterns = [
    url(r'^perfil-cliente/', PerfilCliente.as_view(), name='perfil_cliente'),
]

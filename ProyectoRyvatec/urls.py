"""ProyectoRyvatec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.ProyectoRyvatecApp.views import Login
from apps.ProyectoRyvatecApp.views import Logout
from apps.ProyectoRyvatecApp.views import Home
from apps.ProyectoRyvatecApp.views import Proveedores
from apps.ProyectoRyvatecApp.views import Tecnicos
from apps.ProyectoRyvatecApp.views import QuienesSomos
from apps.ProyectoRyvatecApp.views import AdicionarUsuario

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^administrador/', include('apps.administrador.urls', namespace='administrador')),
    url(r'^proveedor/', include('apps.proveedor.urls', namespace='proveedor')),
    url(r'^tecnico/', include('apps.tecnico.urls', namespace='tecnico')),
    # url(r'^cliente/', include('apps.cliente.urls', namespace='cliente')),
    url(r'^proveedores/', Proveedores.as_view(), name='proveedores'),
    url(r'^tecnicos/', Tecnicos.as_view(), name='tecnicos'),
    url(r'^quienes-somos/', QuienesSomos.as_view(), name='quienes_somos'),
    url(r'^adicionar-usuarios/', AdicionarUsuario.as_view(), name='adicionar_usuarios')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

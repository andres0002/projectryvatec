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
from ProyectoRyvatecApp.views import Login
from ProyectoRyvatecApp.views import Logout
from django.conf.urls import include
from django.conf import settings
from ProyectoRyvatecApp.views import Home

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^$', Home.as_view((), name='home')),
    url(r'^administrador/', include('administrador.urls', namespace='administrador')),
    url(r'^proveedor/', include('proveedor.urls', namespace='proveedor')),
    url(r'^tecnico/', include('tecnico.urls', namespace='tecnico')),
    # url(r'^cliente/', include('cliente.urls', namespace='cliente')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.base import View
from django.shortcuts import render

from ProyectoRyvatecApp.models import Usuario
from ProyectoRyvatecApp.forms import UsuarioForm

# Create your views here.

class PerfilCliente(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'cliente/perfil_cliente.html'
    form_class = UsuarioForm

    def get(self, request):
        try:
            datos_usuario = Usuario.objects.get(usuid=request.user.pk)
            form = self.form_class(instance=datos_usuario)
            return render(request, self.template_name, {'form': form})

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        try:
            datos_usuario = Usuario.objects.get(usuid=request.user.pk)
            form = self.form_class(request.POST, instance=datos_usuario)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Perfil se modificó correctamente')
            else:
                messages.add_message(request, messages.ERROR, 'El Perfil no se pudo modificar')

            return self.get(request)

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

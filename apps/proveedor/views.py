# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.base import View
from django.shortcuts import render
from apps.ProyectoRyvatecApp.models import Usuario
from apps.ProyectoRyvatecApp.models import Dispositivo
from apps.ProyectoRyvatecApp.forms import UsuarioForm
from apps.ProyectoRyvatecApp.forms import DispositivoForm

# Create your views here.

class PerfilProveedor(LoginRequiredMixin, View):
    '''
        Esta clase se encarga de visualizar y  modificar los datos personales del usuario que se encuentra logeado..
    '''
    login_url = '/'
    template_name = 'proveedor/perfil_proveedor.html'
    form_class = UsuarioForm

    def get(self, request):
        '''
        Eata funcion nos muestra el formulario de los datos personales del ususario registrado o que se encuentra logeado.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de los datos personales con el formulario correspondiente..
        '''
        try:
            datos_usuario = Usuario.objects.get(usuid=request.user.pk)
            form = self.form_class(instance=datos_usuario)
            return render(request, self.template_name, {'form': form})

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        '''
        Esta funcion modifica los datos personales del ususario que se encuentra logeado, valida si se modifico correctamente o si se presento un erro en la modificacion de los datos.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna a la plantilla de los datos personales o perfil.
        '''
        try:
            datos_usuario = Usuario.objects.get(usuid=request.user.pk)
            form = self.form_class(request.POST, request.FILES, instance=datos_usuario)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Perfil se modificó correctamente')
            else:
                messages.add_message(request, messages.ERROR, 'El Perfil no se pudo modificar')

            return self.get(request)

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class ListarDispositivos(LoginRequiredMixin, View):
    '''Esta clase se encargaa de mostrarnos todos los dispositivos correspondientes al ususario logeado.'''
    login_url = '/'
    form_class = DispositivoForm
    template_name = 'proveedor/listar_dispositivos.html'

    def get(self, request):
        '''
        Esta funcion se encarga de mostrarnos la plantilla de listar dispositivos.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla y la lista de todos los dispositivos.
        '''
        datos_usuario = Usuario.objects.get(usuid=request.user.pk)
        list_dispositivos = Dispositivo.objects.filter(usuario=datos_usuario.pk)
        return render(request, self.template_name, {'dispositivos': list_dispositivos})

class AdicionarDispositivo(LoginRequiredMixin, View):
    '''Esta clase se encarga de agregar un nuevo dispositivo al sistema de informacion.'''
    login_url = '/'
    form_class = DispositivoForm
    template_name = 'proveedor/adicionar_dispositivos.html'

    def get(self, request):
        '''
        Esta funcion se encarga de mostrarnos la plantilla de adicionar dispositivo.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de adicionar dispositivo, con sus respectivo formulario.
        '''
        datos_usuario = Usuario.objects.get(usuid=request.user.pk)
        form = self.form_class(datos_usuario)
        return render(request, self.template_name, {'form': form, 'foto_dispositivo': None})

    def post(self, request):
        '''
        Esta funcion se encarga de verificar que el dispositivo se alla agregado corretamente o de lo contrario que no se alla podido agregvar.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la lista de todos los dispositivos registrados en el sistema.
        '''
        datos_usuario = Usuario.objects.get(usuid=request.user.pk)
        form = self.form_class(datos_usuario, request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El dispositivo se adicionó correctamente')

        else:
            messages.add_message(request, messages.ERROR, 'El dispositivo no se pudo adicionar')

        listar = ListarDispositivos()
        return listar.get(request)

class VisualizarDispositivo(LoginRequiredMixin, View):
    '''Esta clase se encarga de visualizar los dispositivos.'''
    login_url = '/'
    form_class = DispositivoForm
    template_name = 'proveedor/visualizar_dispositivos.html'

    def get(self, request, id_dispositivo):
        '''
        Esta funcion se encarga de mostrarnos el dispositivo selecionado.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_dispositivo: Este es el actributo que contiene el identificador del dispositivo para asi poderlo visualizar.
        :return: Nos retorna la plantilla de visualizar el dispositivo y el respectivo formulario.
        '''
        datos_usuario = Usuario.objects.get(usuid=request.user.pk)
        dispositivo = Dispositivo.objects.get(id_dispositivo=id_dispositivo)
        form = self.form_class(datos_usuario, instance=dispositivo)
        return render(request, self.template_name, {'form': form, 'foto_dispositivo': dispositivo.imagen})

class ModificarDispositivo(LoginRequiredMixin, View):
    '''Esta clase se encarga de modificar los  datos del dispositivo.'''
    login_url = '/'
    form_class = DispositivoForm
    template_name = 'proveedor/modificar_dispositivos.html'

    def get(self, request, id_dispositivo):
        '''
                Esta funcion se encarga de mostrar en dispositivo selecionado.
                :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                :param id_dispositivo: Este es el actributo que contiene el identificador del dispositivo para asi poderlo modificar.
                :return: Nos retorna la plantilla de modificar el dispositivo y el respectivo formulario.
                '''
        datos_usuario = Usuario.objects.get(usuid=request.user.pk)
        dispositivo = Dispositivo.objects.get(id_dispositivo=id_dispositivo)
        form = self.form_class(datos_usuario, instance=dispositivo)
        return render(request, self.template_name, {'form': form, 'foto_dispositivo': dispositivo.imagen})

    def post(self, request, id_dispositivo):
        '''
                Esta funcion se encarga de traer el dispositivo selecionado y modificarlo.
                :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                :param id_dispositivo: Este es el actributo que contiene el identificador del dispositivo para asi poderlo modificarlo.
                :return: Nos retorna toda la lista de los dispositivos registrados en el sistema.
                '''
        datos_usuario = Usuario.objects.get(usuid=request.user.pk)
        dispositivo = Dispositivo.objects.get(id_dispositivo=id_dispositivo)
        form = self.form_class(datos_usuario, request.POST, request.FILES, instance=dispositivo)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El dispositivo se modificó correctamente')

        else:
            messages.add_message(request, messages.ERROR, 'El dispositivo no se pudo modificar')

        listar = ListarDispositivos()
        return listar.get(request)

class BorrarDispositivo(LoginRequiredMixin, View):
    '''Esta clase se encarga de borrar los dispositivos.'''
    login_url = '/'
    form_class = DispositivoForm
    template_name = 'proveedor/borrar_dispositivos.html'

    def get(self, request, id_dispositivo):
        '''
        Esta funcion se encarga de mostrar en dispositivo selecionado.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_dispositivo: Este es el actributo que contiene el identificador del dispositivo para asi poderlo borrar.
        :return: Nos retorna la plantilla de borrar el dispositivo y el respectivo formulario.
        '''
        try:
            dispositivo = Dispositivo.objects.get(id_dispositivo=id_dispositivo)
            form = self.form_class(instance=dispositivo)
            return render(request, self.template_name, {'form': form})

        except Dispositivo.DoesNotExist:
            listar = ListarDispositivos()
            return listar.get(request)

    def post(self, request, id_dispositivo):
        '''
        Esta funcion se encarga de traer el dispositivo selecionado y borrarlo.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_dispositivo: Este es el actributo que contiene el identificador del dispositivo para asi poderlo borrar.
        :return: Nos retorna toda la lista de los dispositivos registrados en el sistema.
        '''
        dispositivo = Dispositivo.objects.get(id_dispositivo=id_dispositivo)
        dispositivo.delete()
        messages.add_message(request, messages.INFO, "El dispositivo se borró correctamente")

        listar = ListarDispositivos()
        return listar.get(request)

class Home(LoginRequiredMixin, View):
    '''
        Esta clase se encarga de mostrarnos la plantilla de inicio.
        '''
    template_name = 'proveedor/home.html'
    def get(self, request):
        '''
            Esta funcion se encarga de mostrar todos los dispositivos registrados en el sistema de informacion.
            :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
            :return: Nos retorna la plantilla de inicio y todos los dispositivos registrados en el sistema.
            '''
        lista_dispositivos = Dispositivo.objects.all()
        return render(request, self.template_name, {'list_dispositivos': lista_dispositivos})

class Proveedores(LoginRequiredMixin, View):
    '''
        Esta clase se encarga de mostrar todos los proveedores registrados en el sistema.
        '''
    template_name = 'proveedor/proveedores.html'
    def get(self, request):
        '''
        Esta funcion se encarga de mostrar todos los proveedores registrados en el sistema.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de los proveedores y a todos los proveedores registrados en el sistema.
        '''
        lista_proveedores = Usuario.objects.filter(rol='PRO')
        return render(request, self.template_name, {'list_proveedores': lista_proveedores})

class Tecnicos(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar todos los tecnicos registrados en el sistema.'''
    template_name = 'proveedor/tecnicos.html'
    def get(self, request):
        '''
        Esta funcion se encarga de mostrar todos los tecnicos registrados en el sistema.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de los tecnicos y a todos los tecnicos registrados en el sistema.
        '''
        lista_tecnicos = Usuario.objects.filter(rol='TEC')
        return render(request, self.template_name, {'list_tecnicos': lista_tecnicos})

class QuienesSomos(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrarnos la plantilla de quienes somos.'''
    template_name = 'proveedor/quienes_somos.html'
    def get(self, request):
        '''
        Esta funcion se encarga de mostrar la mision y vision del proyecto ryvatec.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de quienes somos.
        '''
        return render(request, self.template_name)

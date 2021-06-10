# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.ProyectoRyvatecApp.models import Usuario
from apps.ProyectoRyvatecApp.models import Dispositivo
from apps.ProyectoRyvatecApp.forms import AdicionarUsuarioForm
from apps.ProyectoRyvatecApp.forms import UsuarioForm

# Create your views here.

class Login(View):
    template_name = 'login.html'
    '''Esta clase se encarga del logeo del usuario, de verificar que el usuario y la contraseña sean correctas.'''
    def get(self, request):
        '''
        Esta funcion se encarga de mostrar la plantilla del login.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla login.
        '''
        return render(request, self.template_name)

    def post(self, request):
        '''
        Esta funcion se encarga de verificar que el usuario y la contraseña sean correctas.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla correspondiente al usuario y si se presenta un error
        o inconveniente nos retorna la plantilla login.
        '''
        username = request.POST.get("signin_username")
        password = request.POST.get("signin_password")
        usuario = auth.authenticate(username=username, password=password)

        if usuario != None and usuario.is_active:
            auth.login(request, usuario)
            cliente = Usuario.objects.filter(usuid=usuario.pk)

            # if cliente[0].rol == "CLI":
            #     return HttpResponseRedirect(reverse('cliente:perfil_cliente'))

            if cliente[0].rol == "AMD":
                return HttpResponseRedirect(reverse('administrador:home'))

            elif cliente[0].rol == "PRO":
                return HttpResponseRedirect(reverse('proveedor:home'))

            elif cliente[0].rol == "TEC":
                return HttpResponseRedirect(reverse('tecnico:home'))

            else:
                messages.add_message(request, messages.ERROR, "Rol de usuario inexistente")

        else:
            if usuario == None:
                messages.add_message(request, messages.ERROR, "El Usuario no se encuentra registrado")

            else:
                messages.add_message(request, messages.ERROR, "El Usuario esta inactivo")

        return render(request, self.template_name)


class Logout(View):
    '''Esta clase se encarga de mostrar el login.'''
    def get(self, request):
        '''
        Esta clase se encarga de mostrar la plantilla login.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla login.
        '''
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))

class Home(View):
    '''Esta clase se encarga de mostrar la plantilla de inicio.'''
    template_name = 'home.html'
    def get(self, request):
        '''
                    Esta funcion se encarga de mostrar todos los dispositivos registrados en el sistema de informacion.
                    :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                    :return: Nos retorna la plantilla de inicio y todos los dispositivos registrados en el sistema.
                    '''
        lista_dispositivos = Dispositivo.objects.all()
        return render(request, self.template_name, {'list_dispositivos': lista_dispositivos})

class Proveedores(View):
    '''Esta clase se encarga en mostrar la plantilla de proveedores.'''
    template_name = 'proveedores.html'
    def get(self, request):
        '''
                Esta funcion se encarga de mostrar todos los proveedores registrados en el sistema.
                :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                :return: Nos retorna la plantilla de los proveedores y a todos los proveedores registrados en el sistema.
                '''
        lista_proveedores = Usuario.objects.filter(rol='PRO')
        return render(request, self.template_name, {'list_proveedores': lista_proveedores})

class Tecnicos(View):
    '''Esta clase se encarga de mostrar la plantilla de tecnicos.'''
    template_name = 'tecnicos.html'
    def get(self, request):
        '''
                Esta funcion se encarga de mostrar todos los tecnicos registrados en el sistema.
                :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                :return: Nos retorna la plantilla de los tecnicos y a todos los tecnicos registrados en el sistema.
                '''
        lista_tecnicos = Usuario.objects.filter(rol='TEC')
        return render(request, self.template_name, {'list_tecnicos': lista_tecnicos})

class QuienesSomos(View):
    '''Esta clase se encarga de mostrarnos la plantilla de quienes somos.'''
    template_name = 'quienes_somos.html'
    def get(self, request):
        '''
                Esta funcion se encarga de mostrar la mision y vision del proyecto ryvatec.
                :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                :return: Nos retorna la plantilla de quienes somos.
                '''
        return render(request, self.template_name)

class AdicionarUsuario(View):
    '''Esta clase se encarga de agregar los usuarios.'''
    form_class = AdicionarUsuarioForm
    template_name = 'adicionar_usuarios.html'

    def get(self, request):
        '''
        Esta funcion se encarga de mostrarnos la plantilla de adicionar usuario y su respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla adicionar usuario y su respectivo formulario.
        '''
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        '''
        Esta funcion se encarga de verificar que el usuario se agrego correctamente o de lo contrario si se precento
        algun inconveniente o error.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna a la plantilla adicionar usuario.
        '''
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        correo = request.POST.get('correo', None)
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        cedula = request.POST.get('id_user', None)
        nombres = request.POST.get('nombre', None)
        apellidos = request.POST.get('apellido', None)
        telefono = request.POST.get('telefono', None)
        pagina = request.POST.get('pagina', None)
        #imagen = request.FILES('imagen', None)
        direccion = request.POST.get('direccion', None)
        rol = request.POST.get('rol', None)

        if password == confirm_password:
            if username and email and password and confirm_password:
                user, created = User.objects.get_or_create(username=username,
                                                            email=email,
                                                            first_name=nombres,
                                                            last_name=apellidos)

                if created:
                    user.set_password(password)
                    user.save()
                    cliente = Usuario(id_user=cedula,
                                        nombre=nombres,
                                        apellido=apellidos,
                                        telefono=telefono,
                                        direccion=direccion,
                                        correo=correo,
                                        pagina=pagina,
                                        #imagen=imagen,
                                        rol=rol,
                                        usuid=user)
                    cliente.save()
                    messages.add_message(request, messages.INFO, "El usuario se agrego satisfactoriamente")

                else:
                    messages.add_message(request, messages.ERROR, "El usuario ya existe en el sistema")

            else:
                messages.add_message(request, messages.ERROR, "Faltan campos por llenar en el formulario")

        else:
            messages.add_message(request, messages.ERROR, "Verifique las contraseña")

        return render(request, self.template_name)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.base import View
from django.shortcuts import render
from django.contrib.auth.models import User
from apps.ProyectoRyvatecApp.models import Usuario
from apps.ProyectoRyvatecApp.models import Dispositivo
from apps.ProyectoRyvatecApp.models import Categoria
from apps.ProyectoRyvatecApp.forms import AdicionarUsuarioForm
from apps.ProyectoRyvatecApp.forms import UsuarioForm
from apps.ProyectoRyvatecApp.forms import DispositivoForm
from apps.ProyectoRyvatecApp.forms import CategoriaForm

# Create your views here.
class PerfilAdministrador(LoginRequiredMixin, View):
    '''
        Esta clase se encarga de visualizar y  modificar los datos personales del usuario que se encuentra logeado..
    '''
    login_url = '/'
    template_name = 'administrador/perfil_administrador.html'
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
        :return: Nos retorna a la plantilla de la lista de los usuarios registrados en el ssistema de informacion.
        '''
        try:
            datos_usuario = Usuario.objects.get(usuid=request.user.pk)
            form = self.form_class(request.POST, request.FILES, instance=datos_usuario)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Perfil se modificó correctamente')

            else:
                messages.add_message(request, messages.ERROR, 'El Perfil no se pudo modificar')

            listar = ListadoUsuarios()
            return listar.get(request)

        except Usuario.DoesNotExist:
            return render(request, "pages-404.html")

class ListadoUsuarios(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar todos los usuarios registrados en el sistema.'''
    login_url = '/'
    template_name = 'administrador/listar_usuarios.html'
    form_class = UsuarioForm

    def get(self, request):
        '''
        Esta funcion se encarga de mostrar todos los usuarios registrados en el sistema.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de listar usuarios y la lista de todos los usuarios.
        '''
        lista_usuarios = Usuario.objects.all()
        return render(request, self.template_name, {'usuarios': lista_usuarios})

class AdicionarUsuario(LoginRequiredMixin, View):
    '''Esta clase se encarga de adicionar los usuarios.'''
    login_url = '/'
    form_class = UsuarioForm
    template_name = 'administrador/adicionar_usuarios.html'

    def get(self, request):
        '''
        Esta funcion  se encarga de mostrar la plantilla de adicionar usuario y sus respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return:Nos retorna la plantilla y el respectivo formulario.
        '''
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        '''
        Esta funcion se encarga de verificar que el usuario se alla agregado correctamente o de lo contrario que no se alla podido agregar.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la lista de todos los usuarios del sistema.
        '''
        # username = request.POST.get('username', None)
        # email = request.POST.get('email', None)
        # correo = request.POST.get('correo', None)
        # password = request.POST.get('password', None)
        # confirm_password = request.POST.get('confirm_password', None)
        # cedula = request.POST.get('id_user', None)
        # nombres = request.POST.get('nombre', None)
        # apellidos = request.POST.get('apellido', None)
        # telefono = request.POST.get('telefono', None)
        # pagina = request.POST.get('pagina', None)
        # imagen = request.FILE('imagen', None)
        # direccion = request.POST.get('direccion', None)
        # rol = request.POST.get('rol', None)
        #
        # if password == confirm_password:
        #     if username and email and password and confirm_password:
        #         user, created = User.objects.get_or_create(username=username,
        #                                                    email=email,
        #                                                    first_name=nombres,
        #                                                    last_name=apellidos)
        #
        #         if created:
        #             user.set_password(password)
        #             user.save()
        #             cliente = Usuario(id_user=cedula,
        #                               nombre=nombres,
        #                               apellido=apellidos,
        #                               telefono=telefono,
        #                               direccion=direccion,
        #                               correo=correo,
        #                               pagina=pagina,
        #                               imagen=imagen,
        #                               rol=rol,
        #                               usuid=user)
        #             cliente.save()
        #             messages.add_message(request, messages.INFO, "El usuario se agrego satisfactoriamente")
        #             list = ListadoUsuarios()
        #             return list.get(request)
        #
        #         else:
        #             messages.add_message(request, messages.ERROR, "El usuario ya existe en el sistema")
        #
        #     else:
        #         messages.add_message(request, messages.ERROR, "Faltan campos por llenar en el formulario")
        #
        # else:
        #     messages.add_message(request, messages.ERROR, "Verique las contraseña")
        #
        # form = self.form_class(request.POST)
        # return render(request, self.template_name, {'form': form})

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El usuario se adicionó correctamente')

        else:
            messages.add_message(request, messages.ERROR, 'El usuario no se pudo adicionar')

        lista = ListadoUsuarios()
        return lista.get(request)

class VisualizarUsuario(LoginRequiredMixin, View):
    '''Esta clase nos permite visualizar los datos personales de un usuario.'''
    login_url = '/'
    form_class = UsuarioForm
    template_name = 'administrador/visualizar_usuario.html'

    def get(self, request, id_usuario):
        '''
        Esta funcion se encarga de mostrarnos la plantilla de visualizar el usuario y sus respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_usuario: Este actributo nos sirve para identificar el usuario que desea visualizar.
        :return: Nos retorna la plantilla de visualizar usuario y su respectivo formulario.
        '''
        cedula_cliente = Usuario.objects.get(id_user=id_usuario)
        form = self.form_class(instance=cedula_cliente)
        return render(request, self.template_name, {'form': form})

class ModificarUsuario(LoginRequiredMixin, View):
    '''Esta clase se encarga de modificar el usuario.'''
    login_url = '/'
    form_class = UsuarioForm
    template_name = 'administrador/modificar_usuario.html'

    def get(self, request, id_usuario):
        '''
        Esta funcion se encarga de mostrar la plantilla de modificar usuario y su respectivo formulario del usuario selecionado.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_usuario: Este actributo nos sirve para identificar al ususario que deseamos modificar.
        :return: Nos retorna la plantilla de modificar usuario y su respectivo formulario
        '''
        cedula_cliente = Usuario.objects.get(id_user=id_usuario)
        form = self.form_class(instance=cedula_cliente)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id_usuario):
        '''
        Esta funcion se encarga de verificar si el usuario se modifico correctamente o de lo contrario si se precento un error.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_usuario: Este actributo nos sirve para identificar al ususario que deseamos modificar.
        :return: Nos retorna la lista de todos los usuarios registrados en el sistema.
        '''
        cedula_cliente = Usuario.objects.get(id_user=id_usuario)
        form = self.form_class(request.POST, request.FILES, instance=cedula_cliente)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El usuario se modificó correctamente')

        else:
            messages.add_message(request, messages.ERROR, 'El usuario no se pudo modificar')

        listar = ListadoUsuarios()
        return listar.get(request)

class BorrarUsuario(LoginRequiredMixin, View):
    '''Esta clase se encarga de eliminar al usuario.'''
    login_url = '/'
    form_class = UsuarioForm
    template_name = 'administrador/borrar_usuario.html'

    def get(self, request, id_usuario):
        '''
        Esta funcion se encarga de mostrar la plantilla de borrar usuario y su respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_usuario: Este actributo nos sirve para identificsr al usuario que deseamos eliminar o borrar.
        :return: Nos retorna la plantilla de borrar usuario y su respectivo formulario.
        '''
        try:
            cedula_cliente = Usuario.objects.get(id_user=id_usuario)
            form = self.form_class(instance=cedula_cliente)
            return render(request, self.template_name, {'form': form})

        except Usuario.DoesNotExist:
            listar = ListadoUsuarios()
            return listar.get(request)

    def post(self, request, id_usuario):
        '''
        Esta funcion se encarga de verificar si el usuario se borro correctamente o de lo contrario si se precento un error.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_usuario: Este actributo sirve para identificar al ususrio que se desea eliminar o borrar.
        :return: Nos retorna La lista de todos los usuarios registrados en el sistema.
        '''
        cedula_cliente = Usuario.objects.get(id_user=id_usuario)
        cedula_cliente.delete()
        messages.add_message(request, messages.INFO, "El usuario se borró correctamente")

        listar = ListadoUsuarios()
        return listar.get(request)

class ListarCategoria(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar una lista de todas las categorias registradas en el sistema.'''
    login_url = '/'
    form_class = CategoriaForm
    template_name = 'administrador/listar_categoria.html'

    def get(self, request):
        '''
        Esta funcion se encarga de mostrar la plantilla de listar categorias.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de listar categorias y la respectiva lista de las categorias.
        '''
        categorias = Categoria.objects.all()
        return render(request, self.template_name, {'categorias': categorias})

class AdicionarCategoria(LoginRequiredMixin, View):
    '''Esta clase se encarga  de adicionar las categorias.'''
    login_url = '/'
    form_class = CategoriaForm
    template_name = 'administrador/adicionar_categoria.html'

    def get(self, request):
        '''
        Esta funcion se encarga de mostrar la plantilla de adicionar categoria y su respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la plantilla de adicionar categoria y  su respectivo formulario.
        '''
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        '''
        Esta funcion se encarga de verificar si la categoria se adiciono correctamente o de lo contrario si se precento algun inconveniente o error.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :return: Nos retorna la lista de todas las categorias registradas en el sistema.
        '''
        try:
            form = self.form_class(request.POST)

            if form.is_valid:
                form.save()
                messages.add_message(request, messages.INFO, 'La categoria se adicionó correctamente')

            else:
                messages.add_message(request, messages.ERROR, 'La categoria no se pudo adicionar')

        except Categoria.DoesNotExist:
            return render(request, "pages-404.html")

        listar = ListarCategoria()
        return listar.get(request)

class VisualizarCategoria(LoginRequiredMixin, View):
    '''
    Esta clase se encarga de visualizar la categoria.
    '''
    login_url = '/'
    form_class = CategoriaForm
    template_name = 'administrador/visualizar_categoria.html'

    def get(self, request, id_categoria):
        '''
        Esta funcion se encarga de visualizar la categoria selecionada.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_categoria: Este actributo sirve para identificar la categoria que seamos visualizar.
        :return: Nos retorna la plantilla visualizar categoria y  su respectivo formulario.
        '''
        categoria = Categoria.objects.get(id_categoria=id_categoria)
        form = self.form_class(instance=categoria)
        return render(request, self.template_name, {'form': form})

class ModificarCategoria(LoginRequiredMixin, View):
    '''Esta clase se encarga de modificar la categoria.'''
    login_url = '/'
    form_class = CategoriaForm
    template_name = 'administrador/modificar_categoria.html'

    def get(self, request, id_categoria):
        '''
        Esta funcion se encarga de mostrar la plantilla modificar categoria y su respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_categoria: Este actributo sirve para identificar la categoria que deseamos modificar.
        :return: Nos retorna la plantilla modificar categoria y su respectivo formulario.
        '''
        categoria = Categoria.objects.get(id_categoria=id_categoria)
        form = self.form_class(instance=categoria)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id_categoria):
        '''
        Esta funcion se encarga de verificar que la categoria se alla modificado correctamente o  de lo contrario si se precento un error.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_categoria: Este actributo sirve para identificar la categoria que se desea modificar.
        :return: Nos retorna la lista de todas las categorias registradas en el sistema.
        '''
        categoria = Categoria.objects.get(id_categoria=id_categoria)
        form = self.form_class(request.POST, instance=categoria)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'La categoria se modificó correctamente')
            listar = ListarCategoria()
            return listar.get(request)

        else:
            messages.add_message(request, messages.ERROR, 'La categoria no se pudo modificar')

        listar = ListarCategoria()
        return listar.get(request)

class BorrarCategoria(LoginRequiredMixin, View):
    '''Esta clase se encarga de borrar las categorias.'''
    login_url = '/'
    form_class = CategoriaForm
    template_name = 'administrador/borrar_categoria.html'

    def get(self, request, id_categoria):
        '''
        Esta funcion nos muestra la plantilla borrar categoria y su respectivo formulario.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_categoria: Este actributo sirve para identificar la categoria que desea eliminar.
        :return: Nos retorna la plantilla borrar categoria y su respectivo formulario.
        '''
        try:
            categoria = Categoria.objects.get(id_categoria=id_categoria)
            form = self.form_class(instance=categoria)
            return render(request, self.template_name, {'form': form})

        except Categoria.DoesNotExist:
            listar = ListarCategoria()
            return listar.get(request)

    def post(self, request, id_categoria):
        '''
        Esta funcionse encarga de verificar que la categoria se alla borrado correctamente o de lo contrario si se precento algun inconveniente.
        :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
        :param id_categoria: Este actributo sirve para identificar la categoria que se desea eliminar.
        :return: Nos retorna la lista de todas las categorias registradas en el sistema.
        '''
        categoria = Categoria.objects.get(id_categoria=id_categoria)
        categoria.delete()
        messages.add_message(request, messages.INFO, "La categoria se borró correctamente")

        listar = ListarCategoria()
        return listar.get(request)

class Home(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar la plantilla de inicio.'''
    template_name = 'administrador/home.html'
    def get(self, request):
        '''
                    Esta funcion se encarga de mostrar todos los dispositivos registrados en el sistema de informacion.
                    :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                    :return: Nos retorna la plantilla de inicio y todos los dispositivos registrados en el sistema.
                    '''
        lista_dispositivos = Dispositivo.objects.all()
        return render(request, self.template_name, {'list_dispositivos': lista_dispositivos})

class Proveedores(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar la plantilla de proveedores.'''
    template_name = 'administrador/proveedores.html'
    def get(self, request):
        '''
                Esta funcion se encarga de mostrar todos los proveedores registrados en el sistema.
                :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                :return: Nos retorna la plantilla de los proveedores y a todos los proveedores registrados en el sistema.
                '''
        lista_proveedores = Usuario.objects.filter(rol='PRO')
        return render(request, self.template_name, {'list_proveedores': lista_proveedores})

class Tecnicos(LoginRequiredMixin, View):
    '''Esta clase se encarga de mostrar la plantilla tecnicos.'''
    template_name = 'administrador/tecnicos.html'
    def get(self, request):
        '''
                Esta funcion se encarga de mostrar todos los tecnicos registrados en el sistema.
                :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                :return: Nos retorna la plantilla de los tecnicos y a todos los tecnicos registrados en el sistema.
                '''
        lista_tecnicos = Usuario.objects.filter(rol='TEC')
        return render(request, self.template_name, {'list_tecnicos': lista_tecnicos})

class QuienesSomos(LoginRequiredMixin, View):
    '''Esta clase se encargade mostrar la plantilla quienes somos.'''
    template_name = 'administrador/quienes_somos.html'
    def get(self, request):
        '''
                Esta funcion se encarga de mostrar la mision y vision del proyecto ryvatec.
                :param request: Objeto que contiene todos los parametros enviados por la peticion del cliente al servidor.
                :return: Nos retorna la plantilla de quienes somos.
                '''
        return render(request, self.template_name)

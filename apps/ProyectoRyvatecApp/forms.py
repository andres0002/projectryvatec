# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from apps.ProyectoRyvatecApp.models import Usuario
from apps.ProyectoRyvatecApp.models import Dispositivo
from apps.ProyectoRyvatecApp.models import Categoria
from apps.ProyectoRyvatecApp.models import ROL_CHOICES


class UsuarioForm(forms.ModelForm):
    '''Esta clase se encarga de definir la estructura del formulario de datos del usuario.'''
    class Meta:
        '''Esta se encarga de definir la estructura del formulario.'''
        model = Usuario
        fields = "__all__"
        labels = {
            'id_user': _(u'Número de Identificacion:'),
            'nombre': _(u'Nombre:'),
            'apellido': _(u'Apellido:'),
            'telefono': _(u'Telefono:'),
            'direccion': _(u'Direccion:'),
            'correo': _(u'Email'),
            'pagina': _(u'Pagina Web'),
            'imagen': _(u'Foto usuario o Logotipo'),
            'especialidad': _(u'Especialidad'),
            'usuid': _(u'Username:'),
            'rol': _(u'Tipo de usuario')
        }

    def __init__(self, *args, **kwargs):
        '''
                Esta funcion se encarga de darle el diseño al formulario.
                :param args: La cantidad de argumentos que recibe.
                :param kwargs: Se encarga de tomar los parametros de la url.
                '''
        super(UsuarioForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class DispositivoForm(forms.ModelForm):
    '''Esta clase se encarga de definir la estructura del formulario de datos del dispositivo.'''
    class Meta:
        '''Esta se encarga de definir la estructura del formulario.'''
        model = Dispositivo
        fields = "__all__"
        labels = {
            'id_dispositivo': _(u'Codigo Dispositivo:'),
            'usuario': _(u'Nombre Usuario:'),
            'categoria': _(u'Nombre Categoria:'),
            'nombre': _(u'Nombre Dispositivo:'),
            'precio': _(u'Precio del Dispositivo'),
            'imagen': _(u'Imagen del Dispositivo'),
            'descripcion': _(u'Descripcion')
        }

    def __init__(self, dispositivo=None, *args, **kwargs):
        '''
                Esta funcion se encarga de darle el diseño al formulario.
                :param args: La cantidad de argumentos que recibe.
                :param kwargs: Se encarga de tomar los parametros de la url.
                '''
        super(DispositivoForm, self).__init__(*args, **kwargs)

        # if dispositivo is not None:
        #     self.fields['datid'].widget = forms.HiddenInput()
        #     self.fields['datid'].initial = dispositivo

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class CategoriaForm(forms.ModelForm):
    '''Esta clase se encarga de definir la estructura del formulario de datos de la categoria..'''
    class Meta:
        '''Esta se encarga de definir la estructura del formulario.'''
        model = Categoria
        fields = "__all__"
        labels = {
            'id_categoria': _(u'Codigo Categoria:'),
            'nombre': _(u'Nombre Categoria:')
        }

    def __init__(self, *args, **kwargs):
        '''
                Esta funcion se encarga de darle el diseño al formulario.
                :param args: La cantidad de argumentos que recibe.
                :param kwargs: Se encarga de tomar los parametros de la url.
                '''
        super(CategoriaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AdicionarUsuarioForm(forms.Form):
    '''Esta clase se encarga de definir la estructura del formulario de datos del usuario.'''
    username = forms.CharField(max_length=150, label='Username')
    email = forms.EmailField(max_length=150, label='Email')
    correo = forms.EmailField(max_length=150, label='Confirme Email')
    password = forms.CharField(max_length=128, label='Contraseña', widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, label='Confirmar Contraseña', widget=forms.PasswordInput())
    id_user = forms.CharField(max_length=10, label='Cedula')
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=30, label='Apellido')
    telefono = forms.CharField(max_length=15, label='Telefono')
    direccion = forms.CharField(max_length=60, label='Direccion')
    pagina = forms.CharField(max_length=150, label='Pagina Web')
    imagen = forms.ImageField()
    especialidad = forms.CharField(max_length=100, label='Especialidad')
    rol = forms.ChoiceField(choices=ROL_CHOICES, label='Tipo de Ususario', widget=forms.Select())

    def __init__(self, *args, **kwargs):
        '''
        Esta funcion se encarga de darle el diseño al formulario.
        :param args: La cantidad de argumentos que recibe.
        :param kwargs: Se encarga de tomar los parametros de la url.
        '''
        super(AdicionarUsuarioForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
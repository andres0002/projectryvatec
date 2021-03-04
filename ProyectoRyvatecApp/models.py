# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

ROL_CHOICES = (
    ('AMD', u'Administrador'),
    # ('CLI', u'Cliente'),
    ('PRO', u'Proveedor'),
    ('TEC', u'Tecnico')
)

class Usuario(models.Model):
    '''
    Esta clase se encarga de definir los actributos de la tabla Usuario de la base de datos ryvatec.
    '''
    id_user = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=60)
    correo = models.EmailField(max_length=150, blank=True, null=True)
    pagina = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='usuarios', default='usuarios/ironman.jpg')
    especialidad = models.CharField(max_length=100)
    usuid = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    def __str__(self):  # __unicode__
        return self.nombre

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"

class Categoria(models.Model):
    '''Esta clase se encarga de definir los actributos de la tabla Categoria de la base de datos ryvatec.'''
    id_categoria = models.CharField(primary_key=10, max_length=10)
    nombre = models.CharField(max_length=30)

    def __str__(self):  # __unicode__
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"

class Dispositivo(models.Model):
    '''Esta clase se encarga de definir los actributos de la tabla Dispositivo de la base de datos ryvatec.'''
    id_dispositivo = models.CharField(primary_key=True, max_length=10)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='dispositivos')
    descripcion = models.CharField(max_length=250)

    def __str__(self):  # __unicode__
        return self.nombre

    class Meta:
        verbose_name_plural = "Dispositivos"
        verbose_name = "Dispositivo"

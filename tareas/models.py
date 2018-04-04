# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
 
# Create your models here.


class Tareas(models.Model):

    descripcion = models.CharField(max_length=250)
    duracion = models.DurationField()
    tiempo_registrado = models.DateTimeField(null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True, blank=True)
    estatus = models.CharField(max_length=1, choices=(('Pendiente','Pendiente'), ('Completada','Completada')), db_index=True, verbose_name='Estatus de tarea')
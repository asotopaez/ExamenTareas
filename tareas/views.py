# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import serializers ,viewsets , generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tareas
from datetime import datetime ,timedelta
from django.db.models import Q
from random import randint
import random
import time

#Funciones para obtener fechas en random()
def strTimeProp(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ptime))

def randomDate(start, end, prop):
    return strTimeProp(start, end,  '%Y-%m-%d %I:%M %p', prop)

#Serializador de Tareas
class TareasSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Tareas
        fields = ('id','descripcion','duracion','tiempo_registrado','estatus')


#List de Tareas.
class TareasList(generics.ListAPIView):

    serializer_class = TareasSerializers

    def get_queryset(self):
        queryset = Tareas.objects.all()
        query = self.request.query_params.get('q', None)
        if query is not None:
            all_results = Tareas.objects.filter(Q(descripcion__icontains=query)|Q(estatus__icontains=query))
            return all_results
        else:
            return queryset

#CRUD de Tareas.
class TareasCRUD(viewsets.ModelViewSet):

    serializer_class = TareasSerializers
    queryset = Tareas.objects.all()
    paginate_by = 10
    paginate_by_param = 'page_size'         

    def update( self , request , pk=None ,):   
        consulta_tarea = Tareas.objects.get(pk=pk)
        serializer = TareasSerializers(consulta_tarea,data = request.data)
        if serializer.is_valid() and consulta_tarea.estatus=="Pendiente":
            serializer.save()
            datos = serializer.data
            return Response(datos)
        else:
            if serializer.errors:
                errors = serializer.errors
            else:
                errors = {"estatus":'Solo actualizar tareas pendientes.'}
        return  Response(errors,status = status.HTTP_400_BAD_REQUEST )

    def destroy(self, request, *args, **kwargs):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

# Creacion de Tareas Automatizadas.
class CreaTareasAPI(APIView):

        def get(self, request, format = None):

            for x in range(0,43):
                fecha = randomDate("2018-04-23 1:30 PM", "2018-04-27 4:50 AM", random.random())
                durationfin = timedelta(seconds=randint(1, 50000))
                Tarea = Tareas(descripcion="Tarea "+str(x),duracion=durationfin,tiempo_registrado=fecha,estatus="Completado")
                Tarea.save()

            for x in range(0,7):
                durationfin = timedelta(seconds=randint(1, 50000))
                Tarea = Tareas(descripcion="Tarea "+str(x),duracion=durationfin,estatus="Pendiente")
                Tarea.save()

            return Response({"msj":"Tareas Creadas."})
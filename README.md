#Prueba de tareas

Dependencias:

Django 1.11
Django Rest Framewok

Syncronizacion y Arranque del proyecto:

1.- python manage.py migrate --settings=ExamenTareas.settings.local

2.- python manage.py runserver --settings=ExamenTareas.settings.local


Servicios:

"Tareas Crud List"

http://localhost:8000/api/tasks/


"Busqueda de Tareas"

http://localhost:8000/api/tasks/searh/?q=Tarea 5

"Creacion automatica de 50 tareas"

http://localhost:8000/api/tasks/craertareas/


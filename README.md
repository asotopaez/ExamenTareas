#Prueba de tareas

Dependencias:

Django 1.11
Django Rest Framewok

Syncronizacion y Arranque del proyecto:

1.- python manage.py migrate --settings=ExamenTareas.settings.local

2.- python manage.py runserver --settings=ExamenTareas.settings.local


Servicios:

"Tareas Crud List"
Metedo: GET,POST,PUT,DELETE
http://localhost:8000/api/tasks/

Metodo: PUT
http://localhost:8000/api/tasks/1


Metodo: DELETE
http://localhost:8000/api/tasks/1

"Busqueda de Tareas"

Metedo: GET
http://localhost:8000/api/tasks/searh/?q=Tarea 5

Metodo: GET
"Creacion automatica de 50 tareas"

http://localhost:8000/api/tasks/craertareas/


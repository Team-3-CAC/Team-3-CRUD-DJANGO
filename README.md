# crud-django

Correr linea de comando

`docker-compose run web django-admin startproject cruddjango .`


Ahora creamos una app que se llama encuestas

`docker-compose run web python manage.py startapp encuestas`


Cada vez que modifiquemos nuestro modelo de datos... vamos a correr el siguiente comando

`docker-compose run web python manage.py migrate`

Por ultimo creamos un super usuario

`docker-compose run web python manage.py createsuperuser`

Actividades:

* Cada Miembro del equipo debe cambiar el archivo readme.md en la seccion de contributors (si no la tiene agregarla)

* Cada miembro del equipo debe poder descargar el proyecto del repositorio y probarlo localmente

* Crear un proyecto de github

* crear N urls con N respuestas distintas dependiendo de la cantidad de miembros del equipo.

* Tienen que tener un test escrito en el archivo tests.py
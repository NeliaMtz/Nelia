# Nelia
Docker Django 
![Guanajuato_LOGO](https://user-images.githubusercontent.com/130393232/235364897-940fd76d-c56a-4e3f-9300-7f9d9893447a.png)
## Sistema Registro de Visitas de Usuarios

Uno de los principales programas de Gobierno del Estado de Guanajuato para asegurdad la calidad es el programa MAS, este programa solicita el registro de cada Usuario que se presenta en una dependencia de gobierno y este sistema consiste en automatizar ese registro de usuarios.

## Índice
  
1. [Base de datos](#id1)

2. [Repositorio](#id2)

3. [Instalacion de Docker](#id3)

4. [Instalacion de Docker Compose](#id4)

5. [Sistema de captura de Visitas](#id5)


## Base de datos <a name="id1"></a>

1. Llenado del registro de visitias de usuarios deberan contener la siguiente información:

* Datos Visita:
  * Identificador de la visita
  * CURP del usuario
  * Fecha de visita
  * Hora de llegada
  * Hora de retirarse
  * identidicador del tramite que realizó
  * CURP de la persona que lo capturó en el sistema

* Datos Usuario:
  * CURP
  * Nombre
  * Apellido Paterno
  * APellido Materno
  * Edad
  * Clave del centro de trabajo en donde labora
  * Escolaridad
  * Funcion
  * email

* Datos del Capturista:
  * CURP de la persona que captura
  * Nombre
  * Puesto
 
* Información de tramites
  * Identificador de tramite
  * Descripción

* Información de Centro de trabajo
  * Clave del centro de trabajo
  * Nombre del centro de trabajo
  
Aqui se representa de manera gráfica la base de datos del sistema, en el cual se puede ver las relaciones entre las tablas y sus campos a detalle.

[Diagrama de BD.pdf](https://github.com/NeliaMtz/Nelia/files/11361778/Diagrama.de.BD.pdf)

Esta imagen se puede generar en linea con la herramienta [dbdiagram.io] y esta puede compartir el diagrama en línea [dbdocs.io].



## Repositorio <a id="id2"></a>

Dentro del repositorio se realizaron los archivos que se encuentran en el proyecto son los siguientes:

* `Info`: Contiene la información del sistema.
* `Registros`: Contiene el proyecto del sistema.
* `README.md`: Contiene la información del sistema.
* `requirements.txt`: Contiene las dependencias del sistema.



## Instalacion de Docker <a name="id3"> </a>

Trabajando sobre plataforma Windows

* Instalar Docker.
Se descarga el instalador de la página https://www.docker.com/products/docker-desktop/ y se ejecuta

Crear entorno virtual
PS C:\Nelia> python3 -m venv venv
Entras a entorno virtual
PS C:\Nelia> .\venv\Scripts\Activate.ps1
Instalas Django 
(venv) PS C:\Nelia> pip install Django
Creas un projecto Django
(venv) PS C:\Nelia> django-admin startproject config .
Ejecta Proyecto
(venv) PS C:\Nelia> python manage.py runserver

* Se crea un nuevo archive manualmente fuera de la ruta de Django

Se llama Dockerfile
Se busca la imagen 
FROM python:3.11.3-alpine3.17

Establecer la ruta en donde se se harán los comandos
WORKDIR /app

Copiar los archivos necesarios para preparar el equipo
COPY ./requirements.txt ./

Instalas y actualizar los paquetes
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip



Primer comando de Docker para construirlo
docker build -t devrrior/docker-django .

(venv) PS C:\Nelia> pip freeze > requirements.txt

Lo corres asi y funciona

docker run devrrior/docker-django
docker run -p 8000:8000 devrrior/docker-django

Pero no corre porque tienes que poner en Dockerfile
ENV PYTHONUNBUFFERED=1

Esta cadena si funciona para levantar el Docker con la cadena del programa
docker run -d -v C:/Nelia/:/app -p 8000:8000 devrrior/docker-django

docker exec -it 1fa3279311bcd2accd985d4f43ed28c6d36babc9cb8d2b5f9f646d6501ee3a81 /bin/sh

para salir ctrl +D

## Instalacion de Docker Compose <a name="id4"> </a>
Levantar el Docker compose
(venv) PS C:\Nelia> docker-compose up

(venv) PS C:\Nelia> docker-compose up -d

(venv) PS C:\Nelia> docker-compose exec django sh

* Crear el archivo `docker-compose.yml` en la carpeta raíz del proyecto.


* Copiar el siguiente código en el archivo `docker-compose.yml`.

  version: '3.9'

services:

  django:
    build: .
    restart: always
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - postgres

  postgres:
    image: postgres:15.2-alpine
    ports:
      - "5431:5432"
    volumes:
      - ./database:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=postgres
  
  pgadmin:
      container_name: pgadmin
      image: dpage/pgadmin4:latest
      environment:
        - PGADMIN_DEFAULT_EMAIL=${PGADMIN_MAIL}
        - PGADMIN_DEFAULT_PASSWORD=${PGADMIN_PW}
      ports:
        - "5050:80"
      restart: always

* Crear el archivo `.env` en la carpeta raíz del proyecto.

  Lo creamos manualmente dentro de la carpeta del proyecto

* Copiar el siguiente código en el archivo `.env`.

POSTGRES_USER=postgres
POSTGRES_PW=postgres
POSTGRES_DB=postgres
POSTGRES_DATA=/var/lib/postgresql/data
PGADMIN_PW=123
PGADMIN_MAIL=marthanelia@gmail.com


* Iniciar Docker Compose.

  (venv) PS C:\Nelia> docker-compose up -d


* Debe de retornar un mensaje como el siguiente:

 [+] Running 3/0
 ✔ Container pgadmin           Running                                                                                           0.0s 
 ✔ Container nelia-postgres-1  Running                                                                                           0.0s 
 ✔ Container nelia-django-1    Running                                                                                           0.0s 

![CapturaDocker](https://user-images.githubusercontent.com/130393232/235364702-28c54c6a-a77a-4a01-9fed-8d4e934af46b.PNG)

* Ingresar al contenedor de Docker.


  docker-compose exec django sh
 
 Instalar pip install django-widget-tweaks
 
* Crear migraciones.

  python manage.py migrate

* Migrar base de datos.

  
  python manage.py migrate
 

* Crear superusuario.

  python manage.py createsuperuser
 

Importante: Ingresar el nombre de usuario, correo electrónico y contraseña.
Username (leave blank to use 'root'): marthanelia@gmail.com
Email address: marthanelia@gmail.com
Password: 123
Password (again): 123
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

* Ingresar a la aplicación.

  http://localhost:8000/
 

* Ingresar a la aplicación de administración.

  http://localhost:8000/admin/
  

* Ingresar a la aplicación de administración de base de datos.

  http://localhost:5050/


## Sistema de Captura de Visitas <a name="id5"> </a>


![CapturaSistemaVisitas](https://user-images.githubusercontent.com/130393232/235564041-89057aa7-dd2e-42d3-b792-9a8b3fd41679.PNG)

Se muestra la pantalla principal del sistema en donde se realizan las capturas de las visitas de usuarios.

Para lograr lo anterior se trabajó en lo siguiente:

Creación de proyecto en Django
C:\Windows\system32>cd..

C:\Windows>cd..

C:\>cd localregistros

C:\localregistros>django-admin startproject registros

C:\localregistros>cd registos
El sistema no puede encontrar la ruta especificada.

C:\localregistros>cd registros

C:\localregistros\registros>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

C:\localregistros\registros>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 27, 2023 - 19:34:43
Django version 4.2, using settings 'registros.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


C:\localregistros\registros>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 27, 2023 - 19:35:26
Django version 4.2, using settings 'registros.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


C:\localregistros\registros>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 27, 2023 - 19:46:55
Django version 4.2, using settings 'registros.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[27/Apr/2023 19:47:00] "GET / HTTP/1.1" 200 10731
[27/Apr/2023 19:47:00] "GET /static/admin/css/fonts.css HTTP/1.1" 404 1816

C:\localregistros\registros>python manage.py runserver

 Hacemos un archivo view.py
 
 
 
Es necesario instalar lo siguiente
 
pip install django-widget-tweaks

pip install django-bootstrap5
pip install --upgrade pip




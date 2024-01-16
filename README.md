# Proyecto-Python-Django
Este es un proyecto realizado para poner en práctica conceptos básicos de Django, Python, algo de HTML y conectado con una base de datos SQLite.

Consiste en un sistema de registros de una universidad que permite gestionar información relacionada con cursos, estudiantes y carreras, es posible realizar consulta, edición y modificación de datos y cuenta con un sistema de autenticación de usuarios con la opción de restablecimiento de contraseña en caso de olvido.

## Instalación
-Tener instalado Python y pip antes de continuar.

-Instalar las dependencias del proyecto: pip install -r requirements.txt

## Ejecución
-Realizar las migraciones de la base de datos: python manage.py makemigrations python manage.py migrate

-Ejecutar el servidor de desarrollo de Django: python manage.py runserver

-Acceder a la aplicación desde el navegador: http://127.0.0.1:8000/

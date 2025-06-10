# TuPrimeraPagina-delaPuente

# Esta es la estructura general del proyecto:

TuPrimeraPagina-delaPuente/
├── Entrega_final/ # Proyecto principal Django (configuración global)
├── autopartes/ # App principal con modelos, vistas, formularios (CRUD de autopartes)
├── accounts/ # App de autenticación de usuarios y perfiles
├── mensajeria/ # App de mensajes entre usuarios
├── templates/ # Templates HTML con herencia desde base.html
├── static/ # Archivos estáticos (CSS, JS, imágenes)
├── media/ # Archivos subidos (imágenes de autopartes)
├── db.sqlite3 # Base de datos SQLite
├── manage.py # Script principal de Django
├── requirements.txt # Dependencias del proyecto
├── .gitignore # Archivos ignorados por Git
└── README.md # Este archivo

*Es recomendable instalar las dependencias utilizadas para el diseño de esta web con el comando:

"pip install -r requirements.txt", previamente habiendo habilitado un entorno virtual

# El orden para probar todas las funcionalidades de la web es el siguiente:

1. Correr el servidor con:

    "python manage.py runserver"

2. Ir al navegador: http://127.0.0.1:8000/

3. Ingresar en "Agregar Marca" para agregar una marca

4. Ingresar en "Agregar Modelo" para agregar un modelo de auto

5. Ingresar en "Agregar Autoparte" para agregar una autoparte de la marca y modelo que ya deben estar ingresados previamente

6. Usar el formulario de busqueda para buscar autopartes por Marca/Modelo/descripcion/nro de serie
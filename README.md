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

*En este proyecto no inclui media/ en el .gitignore. Entiendo que en la consigna solicitan incluir las imagenes
del proyecto en la carpeta static/, pero a fines visuales decidi agregarlas en el media/: 

"""Exista gitignore con:

pycache

db.sqlite3

media

Estos últimos son por el hecho de no compartir la info de tu bd y, aparte, las imágenes son archivos muy pesados que no es recomendable tenerlos en el repo. En cambio, las imágenes que sean parte del código del proyecto deberían guardarse en la carpeta static."""

# El orden para probar todas las funcionalidades de la web es el siguiente:

1. En la terminal de VS Code clona el repositorio:

git clone https://github.com/Santy19950604/TuPrimeraPagina-delaPuente.git


2. Una vez clonado, posicionarse sobre la carpeta:

cd "Tu ruta actual"/TuPrimeraPagina-delaPuente


3. Crear y activar el entorno virtual:

python -m venv venv

venv\Scripts\activate


4. Instalar dependencias del proyecto:

pip install -r requirements.txt


5. Realizar las migraciones de la BD:

python manage.py makemigrations
python manage.py migrate


6. Cargar los datos (Objetos) iniciales para mostrar en la lista (Opcional):

python manage.py loaddata autopartes_iniciales.json

*Esto es lo mencionado anteriormente


7. Crear superusuario para acceder al panel de admin de Django:

python manage.py createsuperuser


8. Iniciar el servidor:

python manage.py runserver


9. Dentro de la url (http://127.0.0.1:8000/), usar los botones para probar cada una de las
funcionalidades requeridas (NavBar, Home, About, Pages, Login, Signup, Messages, Profile, Logout, Get pages, Get page, Create page, Update Page, Delete page, Get profile, Update profile)

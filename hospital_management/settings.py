"""
Django settings for hospital_management project.
"""

from pathlib import Path
import pymysql

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

# Cambia esta clave por una segura en producción y no la expongas públicamente
SECRET_KEY = 'django-insecure-fake-key-for-dev'

# DEBUG en True para desarrollo, False para producción
DEBUG = True

# En desarrollo puede estar vacío, en producción coloca dominios/IPs permitidos
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'users',
    'patients',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hospital_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Puedes agregar aquí rutas a tus templates personalizados si tienes
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hospital_management.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hospital_db',
        'USER': 'root',
        'PASSWORD': 'tu_contraseña',  # Cambia esto por tu contraseña real
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Modelo de usuario personalizado
AUTH_USER_MODEL = 'users.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

LANGUAGE_CODE = 'es'  # Español

TIME_ZONE = 'UTC'  # Puedes cambiarlo a tu zona horaria, ej: 'America/Bogota'

USE_I18N = True

USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'

# En producción deberías definir STATIC_ROOT para collectstatic
# STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "dbempleado",
        "USER": "django",
        "PASSWORD": "django",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

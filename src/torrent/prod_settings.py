import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "46cfb1*xsnj8+gvz#2g(xnn0%v3ss)ax12n73l#+_@*=aa@3rh"

DEBUG = False

# Add domain
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# pg_ctl start -D "C:/Program Files/PostgreSQL/12/data"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'torrent',
        'USER' : 'postgres', 
        'PASSWORD' : '123456',
        'HOST' : '127.0.0.1',
        'PORT' : '5432',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

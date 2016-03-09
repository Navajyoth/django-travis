from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'abcd1234',
        'OPTIONS': {
            # "autocommit": True,
        },
    }
}


#import dj_database_url
#DATABASES = {}
#DATABASES['default'] =  dj_database_url.config()

BASE_URL = "http://app.com/"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'logging@rawdatatech.com'
EMAIL_HOST_PASSWORD = 'Abcd123#$'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

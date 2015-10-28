# -*- coding: utf-8 -*-
from .settings import *
DEBUG = True
SSLIFY_DISABLE = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
TEMPLATE_DEBUG = DEBUG
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DATABASES = {
     'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2', 
             'NAME': 'language2db',  
             'USER': 'muwawa',
             'PASSWORD': DB_PASSWORD,
             'HOST': '',  
             'PORT': '', 
         }
}


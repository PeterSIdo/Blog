# c:/Users/Peter/Blog/Blog/settings/dev.py |||
from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sy(fuc=@e57xb_9@ir88lj0pyud7nn#0robo!uapjag4i)#84t'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
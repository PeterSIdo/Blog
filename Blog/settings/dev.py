# c:/Users/Peter/Blog/Blog/settings/dev.py |||
from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sy(fuc=@e57xb_9@ir88lj0pyud7nn#0robo!uapjag4i)#84t'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*']
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# SSL/HTTPS Settings for Development
SECURE_SSL_REDIRECT = False  # Don't force HTTPS in development
CSRF_COOKIE_SECURE = True  # Set to True to ensure CSRF cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Set to True to ensure session cookies are only sent over HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Required for proper HTTPS detection behind a proxy
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS filtering in browsers
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking
SECURE_HSTS_SECONDS = 0  # Disable HSTS in development
SECURE_HSTS_INCLUDE_SUBDOMAINS = False  # Disable HSTS subdomains in development
SECURE_HSTS_PRELOAD = False  # Disable HSTS preloading in development
USE_X_FORWARDED_HOST = True  # Trust X-Forwarded-Host header
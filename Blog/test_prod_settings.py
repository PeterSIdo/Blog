import os
from decouple import Config, RepositoryEnv
import django
from django.core.management import execute_from_command_line
from django.db import connections
from django.db.utils import OperationalError
# Load test environment variables
env_file = '.env.test'
env_config = Config(RepositoryEnv(env_file))
# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'Blog.settings.prod'
os.environ.update({
    'DATABASE_URL': env_config('DATABASE_URL'),
    'DJANGO_SECRET_KEY': env_config('DJANGO_SECRET_KEY'),
    'DJANGO_DEBUG': env_config('DJANGO_DEBUG'),
    'DJANGO_ALLOWED_HOSTS': env_config('DJANGO_ALLOWED_HOSTS'),
    'CSRF_TRUSTED_ORIGINS': env_config('CSRF_TRUSTED_ORIGINS')
})
# Initialize Django
django.setup()
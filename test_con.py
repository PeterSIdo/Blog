# Test database connection
from django.db import connections
try:
    connections['default'].ensure_connection()
    print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")
# Test environment variables
from django.conf import settings
print(f"DEBUG: {settings.DEBUG}")
print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
print(f"DATABASE URL: {settings.DATABASES['default']['NAME']}")
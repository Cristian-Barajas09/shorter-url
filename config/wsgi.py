"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from decouple import config as env_config

from django.core.wsgi import get_wsgi_application

environment = env_config("DJANGO_ENV", default="production", cast=str)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.settings.{environment}')

application = get_wsgi_application()

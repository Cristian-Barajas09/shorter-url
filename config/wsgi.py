"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

environment = os.environ.get("DJANGO_ENV", "production")
os.environ["DJANGO_SETTINGS_MODULE"] = f'config.settings.{environment}'

application = get_wsgi_application()

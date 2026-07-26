"""develop settings"""

# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from config.settings.base import *
# pylint: enable=wildcard-import
# pylint: enable=unused-wildcard-import

DEBUG = True
SECRET_KEY = 'django-insecure-j=b+tp%2x1bm=#pqgo$i34hqly5*-p^q0ltytnr7ryl0%^uso4'


# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["localhost", '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

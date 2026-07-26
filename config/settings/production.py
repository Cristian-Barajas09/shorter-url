"""production settings"""
import dj_database_url
from decouple import config

# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from config.settings.base import *
# pylint: enable=wildcard-import
# pylint: enable=unused-wildcard-import

DEBUG = False

ALLOWED_HOSTS = ["localhost", '127.0.0.1']


url: str = config('DATABASE_URL', cast=str) # type: ignore

DATABASES = {
    'default': dj_database_url.config(
        default=url,
        conn_max_age=600,
        conn_health_checks=True,
    )
}

"""production settings"""

import dj_database_url
from decouple import config, Csv

# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from config.settings.base import *

# pylint: enable=wildcard-import
# pylint: enable=unused-wildcard-import

DEBUG = False


ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv()
)


url: str = config("DATABASE_URL", cast=str)  # type: ignore

DATABASES = {
    "default": dj_database_url.config(
        default=url,
        conn_max_age=600,
        conn_health_checks=True,
    )
}

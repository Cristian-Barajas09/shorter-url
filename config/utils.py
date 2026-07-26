"""utils for config"""
import string
import random
from django.db import models

class AuditQuerySet(models.QuerySet):
    """audit query set"""

    def active(self):
        """get the active models"""
        return self.filter(deleted_at__isnull=True)

class AuditManager(models.Manager):
    """audit manager"""

    def get_queryset(self) -> models.QuerySet:
        """get query set"""
        return AuditQuerySet(self.model, using=self._db)


class AuditModel(models.Model):
    """audit model"""

    audit = AuditManager.from_queryset(AuditQuerySet)()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


    class Meta:
        """config for this model"""

        abstract = True


def generate_random_code():
    """generate random code for urls"""
    characters_seed = string.ascii_lowercase + string.digits + "-"

    return ''.join(random.choice(characters_seed) for _ in range(10))

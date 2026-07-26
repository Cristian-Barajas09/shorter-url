"""shorter models"""

from django.db import models
from django.contrib.auth.models import User
from config.utils import AuditModel

class ShortURL(AuditModel):
    """
        Shorter url model for save the environment
    """

    original_url = models.URLField()
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    class Meta(AuditModel.Meta):
        """configuration for this model"""

        db_table = "short_urls"
        indexes = [
            models.Index(fields=["name", "user"])
        ]


    def __str__(self) -> str:
        return f"ShortUrl({self.name}, {self.original_url})"

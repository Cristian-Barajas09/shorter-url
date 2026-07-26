"""shorter admin models"""
from django.contrib import admin
from shorter.models import ShortURL
# Register your models here.

@admin.register(ShortURL)
class ShortUrlModelAdmin(admin.ModelAdmin):
    """short url model admin"""

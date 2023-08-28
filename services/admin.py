from django.contrib import admin
from django.db import models
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass



from django.contrib import admin
from django.db import models
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

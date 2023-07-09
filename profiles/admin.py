from django.contrib import admin
from django.db import models
from .models import Profile
from tinymce.widgets import TinyMCE


class ProfileAdmin(admin.ModelAdmin):
    formfield_overrides= {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Profile, ProfileAdmin)


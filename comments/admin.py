from django.contrib import admin
from django.db import models
from .models import Comment
from tinymce.widgets import TinyMCE


class CommentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Comment, CommentAdmin)


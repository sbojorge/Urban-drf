from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
# signals to implement notifications to the owner of the post about comment created
# from django.db.models.signals import post_save
# from django.dispatch import receiver

class Comment(models.Model):
    """
    Creates a comment instance
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content

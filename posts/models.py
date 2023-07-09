from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video


class Post(models.Model):
    """
    Post model for storing images and/or videos in the database
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='images/', default='../old-time-camera.512x422_iwlbmx', blank=True
    )
    video = models.ImageField(
        upload_to='videos/', default='../film-camera.512x512_qa6tan', blank=True
    )
    content = models.TextField(blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f'{self.id} {self.title}'


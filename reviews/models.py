from django.db import models
from django.contrib.auth.models import User
from services.models import Service


class Review (models.Model):
    """
    Review model for storing user's reviews and ratings in the database
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='reviews'
    )
    content = models.TextField(blank=True)
    rating = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.owner}' review"

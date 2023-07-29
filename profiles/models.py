from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Profile model
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default-user-circle.256x256_qkk4wi'
    )
    location = CountryField(blank_label='(select country)')
    cities = models.TextField(default="Your favorite cities are...")
    content = models.TextField(
        default='What kind of urban adventurer are you (food & drink lover,'
                'festival, sportif, wellness, etc)?'
                'Must visit cities, places to avoid, etc'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"


# Creates a profile every time a user instance is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

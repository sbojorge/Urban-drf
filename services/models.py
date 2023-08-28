from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Service(models.Model):
    """
    Service model for storing service offerings in the database
    """
    SERVICE_CATEGORY = [
        ('TOUR_GUIDE', 'Tour guide'),
        ('ACCOMODATION', 'Accomodation'),
        ('RESTAURANT', 'Restaurant'),
        ('TRAVEL_AGENCY', 'Travel agency'),
        ('OTHER', 'Other'),
        ('SELECT_A_SERVICE_CATEGORY','Select a service category')
    ]    
    category = models.CharField(max_length=100,
        choices=SERVICE_CATEGORY,
        default='SELECT_A_SERVICE_CATEGORY')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='images/', default='../handshake.256x176_vv06fu',
        blank=True
    )
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=255, blank=True)
    website = models.URLField(max_length=200, blank=True)
    facebook_link = models.URLField(max_length=200, blank=True)
    instagram_link = models.URLField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    




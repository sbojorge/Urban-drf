from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
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
    country = CountryField(blank_label='(select country)', blank=True)
    city = models.CharField(max_length=100, blank=True)
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

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.owner}'s service offering details"
    




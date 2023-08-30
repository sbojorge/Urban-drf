from django.contrib.auth.models import User
from .models import Service
from rest_framework import status
from rest_framework.test import APITestCase


class ServiceListCreateViewTests(APITestCase):
    """
    Test retrieving the list of existing services and creating a service
    """

    def setUp(self):
        User.objects.create_user(username='ella', password='rabbit')

    def test_can_list_services(self):
        ella = User.objects.get(username='ella')
        self.client.login(username='ella', password='rabbit')
        Service.objects.create(owner=ella, name='the best resto')
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
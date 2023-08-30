from django.contrib.auth.models import User
from .models import Contact
from rest_framework import status
from rest_framework.test import APITestCase


class ContactListCreateViewTests(APITestCase):
    """
    Test retrieving the list of existing contacts
    and let the authenticated user create a contact
    """

    def setUp(self):
        ella = User.objects.create_user(username='ella', password='rabbit')
        damien = User.objects.create_user(username='damien', password='cat')
        Contact.objects.create(owner=ella, content='I have a suggestion')

    def test_can_list_contacts(self):
        ella = User.objects.get(username='ella')
        self.client.login(username='ella', password='rabbit')
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_contact(self):
        self.client.login(username='ella', password='rabbit')
        ella = User.objects.get(username='ella')
        response = self.client.post('/contacts/', {'reason': 'suggestion',
                                    'content': 'create a forum'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_can_create_contact(self):
        ella = User.objects.get(username='ella')
        response = self.client.post('/contacts/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

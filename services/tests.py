from django.contrib.auth.models import User
from .models import Service
from rest_framework import status
from rest_framework.test import APITestCase


# class ServiceListCreateViewTests(APITestCase):
#     """
#     Test retrieving the list of existing services and creating a service
#     """

#     def setUp(self):
#         User.objects.create_user(username='ella', password='rabbit')

    # def test_can_list_services(self):
    #     ella = User.objects.get(username='ella')
    #     self.client.login(username='ella', password='rabbit')
    #     Service.objects.create(owner=ella, name='the best resto')
    #     response = self.client.get('/services/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_authenticated_user_can_create_service(self):
    #     self.client.login(username='ella', password='rabbit')
    #     response = self.client.post('/services/', {'name': 'the best resto'})
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    # def test_unauthenticated_user_cant_create_service(self):
    #     response = self.client.post('/services/', {'name': 'the best resto'})
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class PostRetrieveUpdateDestroyViewTests(APITestCase):
    """
    Test retrieving a service by id and updating/deleting the service
    if the user owns it
    """

    def setUp(self):
        ella = User.objects.create_user(username='ella', password='rabbit')
        damien = User.objects.create_user(username='damien', password='cat')
        Service.objects.create(
            owner=ella, name='the best resto'
        )
        Service.objects.create(
            owner=damien, name='good sleep hotel'
        )

    # def test_can_retrieve_service_by_valid_id(self):
    #     response = self.client.get('/services/1/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # def test_cant_retrieve_service_by_invalid_id(self):
    #     response = self.client.get('/services/15/')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # def test_user_can_update_owned_service(self):
    #     self.client.login(username='ella', password='rabbit')
    #     response = self.client.put('/services/1/', {'name': 'the best resto'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_user_cant_update_someoneelses_service(self):
    #     self.client.login(username='ella', password='rabbit')
    #     response = self.client.put('/services/2/', {'name': 'good sleep hotel'})
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_user_can_delete_owned_service(self):
    #     self.client.login(username='ella', password='rabbit')
    #     response = self.client.delete('/services/1/')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def test_user_cant_delete_someoneelses_service(self):
    #     self.client.login(username='ella', password='rabbit')
    #     response = self.client.delete('/services/2/')
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

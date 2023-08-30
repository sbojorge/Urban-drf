from django.contrib.auth.models import User
from .models import Review
from services.models import Service
from rest_framework import status
from rest_framework.test import APITestCase


class ReviewListCreateViewTests(APITestCase):
    """
    Test retrieving the list of existing reviews
    and creating a review on a service
    """

    def setUp(self):
        ella = User.objects.create_user(username='ella', password='rabbit')
        Service.objects.create(owner=ella, name='the best resto')

    def test_can_list_review(self):
        ella = User.objects.get(username='ella')
        service = Service.objects.get(id=1)
        self.client.login(username='ella', password='rabbit')
        Review.objects.create(owner=ella, service=service, rating=3)
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_review(self):
        self.client.login(username='ella', password='rabbit')
        service = Service.objects.get(id=1)
        response = self.client.post('/reviews/', {'rating': 3,
                                    'service': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cant_create_review(self):
        service = Service.objects.get(id=1)
        response = self.client.post('/reviews/', {'rating': 3,
                                    'service': 1})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ReviewDetailViewTests(APITestCase):
    """
    Test retrieving a review by id and updating/deleting the review
    if the user owns it
    """

    def setUp(self):
        ella = User.objects.create_user(username='ella', password='rabbit')
        damien = User.objects.create_user(username='damien', password='cat')
        service_e = Service.objects.create(owner=ella,
                                           name='the best resto')
        service_d = Service.objects.create(owner=damien,
                                           name='good sleep hotel')
        Review.objects.create(owner=ella, service=service_e, rating=3)
        Review.objects.create(owner=damien, service=service_d, rating=4)

    def test_can_retrieve_review_by_valid_id(self):
        response = self.client.get('/reviews/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_review_by_invalid_id(self):
        response = self.client.get('/reviews/5/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_authenticated_user_can_update_owned_review(self):
        self.client.login(username='ella', password='rabbit')
        response = self.client.put('/reviews/1/', {'rating': '4'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_someoneelses_review(self):
        self.client.login(username='ella', password='rabbit')
        response = self.client.put('/reviews/2/', {'rating': '3'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_owned_review(self):
        self.client.login(username='damien', password='cat')
        response = self.client.delete('/reviews/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_someoneelses_review(self):
        self.client.login(username='damien', password='cat')
        response = self.client.delete('/reviews/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

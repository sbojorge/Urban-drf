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
        Review.objects.create(owner=ella, service=service, rating= 3)
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_authenticated_user_can_create_comment(self):
    #     self.client.login(username='ella', password='rabbit')
    #     post = Post.objects.get(id=1)
    #     response = self.client.post('/comments/', {'content': 'great post!',
    #                                 'post': 1})
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_unauthenticated_user_cant_create_post(self):
    #     post = Post.objects.get(id=1)
    #     response = self.client.post('/comments/', {'content': 'great post!',
    #                                 'post': 1})
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

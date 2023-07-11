from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class PostListCreateViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='ella', password='rabbit')
    
    def test_can_list_posts(self):
        ella = User.objects.get(username='ella')
        Post.objects.create(owner=ella, title='a city trip')
        client = APIClient()
        response = client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_post(self):
        client = APIClient()
        client.login(username='ella', password='rabbit')
        response = client.post('/posts/', {'title': 'a city trip'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_unauthenticated_user_cant_create_post(self):
        client = APIClient()
        response = client.post('/posts/', {'title': 'a city trip'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class PostRetrieveUpdateDestroyViewTests(APITestCase):
    def setUp(self):
        ella = User.objects.create_user(username='ella', password='rabbit')
        damien = User.objects.create_user(username='damien', password='cat')
        Post.objects.create(
            owner=ella, title='a fun city trip', content='only playgrounds'
        )
        Post.objects.create(
            owner=damien, title='a food city trip', content='only restaurants'
        )
    
    def test_can_retrieve_post_by_valid_id(self):
        client = APIClient()
        response = client.get('/posts/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_by_invalid_id(self):
        client = APIClient()
        response = client.get('/posts/15')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_owned_post(self):
        client = APIClient()
        client.login(username='ella', password='rabbit')
        response = client.put('/posts/1', {'title': 'a game trip'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_cant_update_someoneelses_post(self):
        client = APIClient()
        client.login(username='ella', password='rabbit')
        response = client.put('/posts/2', {'title': 'a sport trip'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
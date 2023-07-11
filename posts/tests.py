from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class PostListCreateViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='ella', password='rabbit')
    
    # def test_can_list_posts(self):
    #     ella = User.objects.get(username='ella')
    #     Post.objects.create(owner=ella, title='a city trip')
    #     client = APIClient()
    #     response = client.get('/posts/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_post(self):
        client = APIClient()
        client.login(username='ella', password='rabbit')
        response = client.post('/posts/', {'title': 'a city trip'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_unauthenticated_user_cant_create_post(self):
        client = APIClient()
        response = client.post('/posts/', {'title': 'a city trip'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    
    

    
        
